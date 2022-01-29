"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])."""

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_beg(self):
        self.assertEqual(max_integer([3, 1, 2]), 3)

    def test_max_neg(self):
        self.assertEqual(max_integer([3, -1, 2]), 3)

    def test_max_negall(self):
        self.assertEqual(max_integer([-3, -1, -2]), -1)

    def test_max_one(self):
        self.assertEqual(max_integer([3]), 3)

    def test_max_empty(self):
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
