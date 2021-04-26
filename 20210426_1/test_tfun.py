import unittest

from tfun import solveSquare


class TestTdfun(unittest.TestCase):

    def test_1_fun(self):
        self.assertEqual(solveSquare(1, -2, 1), (1, 1))

    def test_2_fun(self):
        self.assertEqual(solveSquare(1, 1, 1), None)

    def test_3_fun(self):
        self.assertEqual(solveSquare(1, -3, 2), (1, 2))
