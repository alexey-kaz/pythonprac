import unittest

from figeq import solve


class TestMo(unittest.TestCase):

    def test_zero_a(self):
        self.assertEqual(solve(0.0, -321.0), None)
        self.assertEqual(solve(0.0, 123.0), None)

    def test_non_zero_a(self):
        self.assertEqual(solve(2.0, 4.0), -2.0)
        self.assertEqual(solve(0.2, -4.0), 20.0)
