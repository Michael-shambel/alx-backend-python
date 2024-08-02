#!/usr/bin/env python3
"""
GithubOrgClient is a class that interacts with the GitHub API to fetch
information about GitHub organizations.
"""
from logging import exception
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from unittest.mock import patch, 


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google'),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, orgs, mock_get_json):
        client = GithubOrgClient(orgs)
        client.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{orgs}'
            )

    @patch.object(GithubOrgClient, 'org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/example/repos"
        }
        client = GithubOrgClient('example')
        expected_url = "https://api.github.com/orgs/example/repos"
        result = client._public_repos_url()
        self.assertEqual(result, expected_url)
        # with patch.object(GithubOrgClient):
        #     client = GithubOrgClient()
        #     result = client._public_repos_url()
        #     self.assertEqual(result, ['repo1', 'repo2'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that the _public_repos method returns a list of repos
        """
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/myorg/repos"
                          ) as mock_public_repos_url:
            mock_get_json.return_value = ['repo1', 'repo2']
            client = GithubOrgClient("example")
            repos = client.public_repos()
            self.assertEqual(repos, ['repo1', 'repo2'])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/myorg/repos")
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test that GithubOrgClient.has_license returns the expected result
        """
        client = GithubOrgClient("dummy_org")
        self.assertEqual(client.has_license(repo, license_key),
                         expected_result)
