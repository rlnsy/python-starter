"""
Tests for the package
"""

from unittest import TestCase

class ExampleTestCase(TestCase):
    """
    A Test Case
    """

    def test_true(self):
        """
        An example test
        """
        self.assertEqual(1 + 1, 2,
                "basic addition should work")
