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
