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
        with self.assertRaises(ValueError) as context:
            evaluate("10 / 0")
        self.assertEqual(str(context.exception), "Dzielenie przez zero")

    def test_invalid_char(self):
        with self.assertRaises(ValueError) as context:
            evaluate("5 + a")
        self.assertEqual(str(context.exception), "Nieznany operator")

    def test_consecutive_operators(self):
        with self.assertRaises(ValueError) as context:
            evaluate("5 ++ 3")
        self.assertEqual(str(context.exception), "Nieznany operator")

    def test_missing_spaces(self):
        self.assertEqual(evaluate("5+3"), 8)

    def test_float_numbers_operations(self):
        self.assertAlmostEqual(evaluate("2 * 3.5"), 7.0)

if __name__ == "__main__":
    unittest.main()
