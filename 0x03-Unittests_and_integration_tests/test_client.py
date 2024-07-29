#!/usr/bin/env python3
"""
"""
from logging import exception
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from client import GithubOrgClient


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

    def test_public_repos_url(self):
        with patch.object(GithubOrgClient):
            client = GithubOrgClient()
            result = client._public_repos_url()
            self.assertEqual(result, ['repo1', 'repo2'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        mock_get_json.return_value = ['repo1', 'repo2']
        with patch.object(GithubOrgClient, '_public_repos_url') as mock_url:
            mock_url.return_value = ['repo1', 'repo2']
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos(), ['repo1', 'repo2'])
            mock_get_json.assert_called_once_with('repo1')
            mock_get_json.assert_called_once_with('repo2')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test that GithubOrgClient.has_license returns the expected result"""
        client = GithubOrgClient("dummy_org")
        self.assertEqual(client.has_license(repo, license_key),
                         expected_result)
