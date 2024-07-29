#!/usr/bin/env python3
"""

"""
from logging import exception
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests.get') as mock_get:
            mock_response = mock_get.return_value
            mock_response.json.return_value = test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    class TestClass:
        def a_method(self):
            return 42
        
        @memoize
        def a_property(self):
            return self.a_method()
    
    @patch('TestClass.a_method')
    def test_memoize(self, mock_a_method):
        mock_a_method.return_value = 42
        test_instance = self.TestClass()
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()
        mock_a_method.assert_called_once()
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
