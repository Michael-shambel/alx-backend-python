#!/usr/bin/env python3
"""
Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.
Implement the TestAccessNestedMap.test_access_nested_map_exception method to
test that the method raises the exception when it is supposed to.
Implement the TestGetJson.test_get_json method to test that the method returns
what it is supposed to.
Implement the TestMemoize.test_memoize method to test that the method returns
what it is supposed to.
"""
from logging import exception
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    test case for access_nested_map function
    implementing access_nested_map function which takes a nested map
    and a list of keys and returns the value located at the path
    specified in the keys list
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function
        """
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
    """
    test case for memoize decorator
    implementing memoize which speed up the calling of the function
    when the function called the same argument the function store the
    result and if the function called again with the same argument it will
    return the result without calling the function again
    """

    def test_memoize(self):
        """
        Test memoize decorator
        Define a test class with a method and a memoized property
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            mock_a_method.assert_called_once()
            self.assertEqual(test_instance.a_property, 42)
            mock_a_method.assert_called_once()
