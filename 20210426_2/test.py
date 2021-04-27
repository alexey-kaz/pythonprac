import unittest

from unittest.mock import MagicMock

from model import Model
import sqr


class TestMo(unittest.TestCase):

    def setUp(self):
        self.model = Model()
        self.view = MagicMock()
        self.view.l = {}
        self.model.start(self.view)

    def val(self):
        self.model.square()
        return self.view.l["text"].replace(' ', '')

    # d = 0
    def test_A(self):
        self.view.square = MagicMock(return_value=sqr.solveSquare(1, 4, 4))
        self.assertEqual(self.val(), "-2.0")

    # d > 0
    def test_B(self):
        self.view.square = MagicMock(return_value=sqr.solveSquare(1, 5, 4))
        self.assertEqual(self.val(), "-4.0,-1.0")

    # d < 0
    def test_C(self):
        self.view.square = MagicMock(return_value=sqr.solveSquare(2, 8, 10))
        self.assertEqual(self.val(), "2.0-1.0i,2.0+1.0i")

    # a = 0, b != 0
    def test_D(self):
        self.view.square = MagicMock(return_value=sqr.solveSquare(0, 1, 2))
        self.assertEqual(self.val(), "-2.0")

    # a = 0, b = 0, c != 0
    def test_E(self):
        self.view.square = MagicMock(return_value=sqr.solveSquare(0, 0, 1))
        self.assertEqual(self.val(), "∅")

    # a = b = c = 0
    def test_F(self):
        self.view.square = MagicMock(return_value=sqr.solveSquare(0, 0, 0))
        self.assertEqual(self.val(), "∞")

    # wrong input
    def test_G(self):
        with self.assertRaises(TypeError):
            self.view.square = MagicMock(return_value=sqr.solveSquare(2, "abc", 5))

