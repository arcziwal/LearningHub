import unittest
from calculator20 import evaluate

class TestEvaluateFunction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate("5 + 3"), 8)

    def test_subtraction(self):
        self.assertEqual(evaluate("12 - 2"), 10)

    def test_division(self):
        self.assertEqual(evaluate("10 / 5"), 2.0)

    def test_multiply(self):
        self.assertEqual(evaluate("3 * 5"), 15)

    def test_complex_expressions(self):
        self.assertEqual(evaluate("5 + 4 * 3 - 4 / 2"), 15.0)

    def test_zero_division(self):
        self.assertEqual(evaluate("10 / 0"), "Nie można obliczyć dzielenia przez zero")

    def test_invalid_char(self):
        self.assertEqual(evaluate("5 + a"), "Nieprawidłowe wyrażenie. Sprawdź składnię i użyte znaki")

    def test_consecutive_operators(self):
        self.assertEqual(evaluate("5 ++ 3"), "Nieprawidłowe wyrażenie. Sprawdź składnię i użyte znaki")

    def test_missing_spaces(self):
        self.assertEqual(evaluate("5+3"), 8)

    def test_float_numbers_operations(self):
        self.assertAlmostEqual(evaluate("2 * 3.5"), 7.0)

    def test_float_numbers_valid_format(self):
        self.assertEqual(evaluate("3.14 + 1.2.3"), "Nieprawidłowe wyrażenie. Sprawdź składnię i użyte znaki")

if __name__ == "__main__":
    unittest.main()
