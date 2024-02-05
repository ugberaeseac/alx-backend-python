#!/usr/bin/env python3
"""
parametized a unit test
TestAccessNestedMap inherits from unittest.TestCase
body of the test method should not be longer than 2 lines
returns the correct input
"""


import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        test if method returns correct output
        test with assertEqual that the function returns the expected result
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_result):
        """
        test if exception is raised due to wrong output
        """
        with self.assertRaises(KeyError) as err:
            result = access_nested_map(nested_map, path)
            self.assertEqual(result, err)
