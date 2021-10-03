"""
Tests for the package
"""

from unittest import TestCase
from mathtools import factorial

class ExampleTestCase(TestCase):
    """
    A Test Case
    """

    def test_basic(self):
        """
        An example test
        """
        self.assertEqual(factorial(0), 1)
