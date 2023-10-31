#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
unittests for the function def max_integer(list=[]):
Your test file should be inside a folder tests
You have to use the unittest module
"""


class TestMAxOfList(unittest.TestCase):
    """
    class used for test max_integer function
    """

    def test_positive(self):
        """
        tests positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7]), 7)
        self.assertEqual(max_integer([233.2, 300, 12.23, 6.89, 7.90]), 300)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([8, 4, 6, 8, 8]), 8)
        self.assertEqual(max_integer([2, 4, 6, 4, 8]), 8)

    def test_negative(self):
        """
        tests negative numbers
        """
        self.assertEqual(max_integer([-1, -20, -3]), -1)
        self.assertEqual(max_integer([-1.9, -1.9, -1.9]), -1.9)
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([-5, -3, -1, -4, 0, -2]), 0)

    def test_edgecases(self):
        """
        test Edge Cases
        """
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([5, 2]), 5)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1000000, 5000000, 3000000]), 5000000)
        self.assertEqual(max_integer([-50, 0, 10, -20, 30, -40, 0, 5, 15,
                                      -25, 35, -45, 0, 25, -15, 20, -30, 40,
                                      -10, 50, 0, -5, 45, -35, 30, 0, -20, 10,
                                      -40, 50, -30, 0, 35, -25, 15, -5, 25, 0,
                                      -45, 20, -35, 45, 0, -15, 30, -10, 40,
                                      50, 0, 5, -40, 35, -45, 10, 0, -20, 50,
                                      30, 15, 20, 0, -25, -5, -35, -15, 25, 0,
                                      -50, -40, 5, 30, -20, 98, 35, -10, 20,
                                      45, 10, 0, -30, 15, -25, 25, -5, 0, 40,
                                      -35, 30, -20, 45, 0, -10, 50, -15, 5,
                                      -25, 0, 20, -30, -40, 35, -50, 0, -5,
                                      10, -45, 25, -15, 0, 30, -20, 40, -35,
                                      15]), 98)
