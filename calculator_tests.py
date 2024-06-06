import unittest
from calculator import Calculator, Complex

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 5), 4)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(3, 4), -1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 6), 24)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(-5, -2), 10)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(6, 6), 1.0)
        self.assertAlmostEqual(self.calc.divide(-3, 1), -3.0)
        self.assertAlmostEqual(self.calc.divide(-5, -2), 2.5)

    def test_divide_by_zero(self):
        a = 1
        b = 0
        with self.assertRaises(ValueError):
            self.calc.divide(a, b)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(4, 0.5), 2)
        self.assertEqual(self.calc.power(4, 2), 16)
    
    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(25), 5)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

class TestCalculatorComplex(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_complex(self):
        a = Complex(1, 2)
        b = Complex(3, 4)
        result = self.calc.add(a, b)
        self.assertEqual(result.real, 4)
        self.assertEqual(result.im, 6)

    def test_subtract_complex(self):
        a = Complex(5, 7)
        b = Complex(2, 3)
        result = self.calc.subtract(a, b)
        self.assertEqual(result.real, 3)
        self.assertEqual(result.im, 4)

    def test_multiply_complex(self):
        a = Complex(2, 3)
        b = Complex(4, 5)
        result = self.calc.multiply(a, b)
        self.assertEqual(result.real, -7)
        self.assertEqual(result.im, 22)

    def test_divide_complex(self):
        a = Complex(5, 6)
        b = Complex(1, 2)
        result = self.calc.divide(a, b)
        self.assertAlmostEqual(result.real, 3.4, places=1)
        self.assertAlmostEqual(result.im, -0.8, places=1)

    def test_divide_complex_by_zero(self):
        a = Complex(1, 1)
        b = Complex(0, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(a, b)

class TestCalculatorHistory(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition_to_history(self):
        a = 2
        b = 3
        result = self.calc.add(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "2 + 3 = 5")
        self.calc.clear_history()

    def test_subtract_to_history(self):
        a = 5
        b = 3
        result = self.calc.subtract(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "5 - 3 = 2")
        self.calc.clear_history()

    def test_multiply_to_history(self):
        a = 5
        b = 6
        result = self.calc.multiply(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "5 * 6 = 30")
        self.calc.clear_history()

    def test_divide_to_history(self):
        a = 10
        b = 2
        result = self.calc.divide(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "10 / 2 = 5.0")
        self.calc.clear_history()

    def test_power_to_history(self):
        a = 2
        b = 10
        result = self.calc.power(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "2 ^ 10 = 1024")
        self.calc.clear_history()

    def test_sqrt_to_history(self):
        a = 16
        result = self.calc.sqrt(a)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "sqrt(16) = 4.0")
        self.calc.clear_history()

    def test_add_complex_to_history(self):
        a = Complex(1, 2)
        b = Complex(3, 4)
        result = self.calc.add(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "(1 + 2i) + (3 + 4i) = 4 + 6i")
        self.calc.clear_history()

    def test_subtract_complex_to_history(self):
        a = Complex(5, 3)
        b = Complex(2, 1)
        result = self.calc.subtract(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "(5 + 3i) - (2 + 1i) = 3 + 2i")
        self.calc.clear_history()

    def test_multiply_complex_to_history(self):
        a = Complex(2, 3)
        b = Complex(4, 5)
        result = self.calc.multiply(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "(2 + 3i) * (4 + 5i) = -7 + 22i")
        self.calc.clear_history()

    def test_divide_complex_to_history(self):
        a = Complex(1, 8)
        b = Complex(2, 3)
        result = self.calc.divide(a, b)
        self.assertEqual(len(self.calc.history), 1)
        self.assertEqual(self.calc.history[0], "(1 + 8i) / (2 + 3i) = 2.0 + 1.0i")
        self.calc.clear_history()

    def test_history_clearing(self):
        result = self.calc.add(1, 1)
        self.assertEqual(len(self.calc.history), 1)
        self.calc.clear_history()
        self.assertEqual(len(self.calc.history), 0)
        

    def test_history_max_10_elements(self):
        for i in range(15):
            result = self.calc.add(1, 1)
        self.assertEqual(len(self.calc.history), 10)
        self.calc.clear_history()

class TestCalculatorEvaluateExpression(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_evaluate_expression_simple(self):
        self.assertEqual(self.calc.evaluate_expression("2 + 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("4 * 5"), 20)
        self.assertEqual(self.calc.evaluate_expression("6 / 2"), 3.0)
        self.assertEqual(self.calc.evaluate_expression("2 ^ 3"), 8)

    def test_evaluate_expression_complex(self):
        self.assertEqual(self.calc.evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(self.calc.evaluate_expression("(2 + 3) * 4"), 20)
        self.assertEqual(self.calc.evaluate_expression("4 * (3 + 2)"), 20)
        self.assertEqual(self.calc.evaluate_expression("2 + (3 * 4) ^ 2"), 146)

    def test_evaluate_expression_with_complex_numbers(self):
        result = self.calc.evaluate_expression("(5 + 6i) / (1 + 2i)")
        self.assertAlmostEqual(result.real, 3.4, places=1)
        self.assertAlmostEqual(result.im, -0.8, places=1)
        result = self.calc.evaluate_expression("(1 + 2i) + (3 + 4i)")
        self.assertEqual(result.real, 4)
        self.assertEqual(result.im, 6)
        result = self.calc.evaluate_expression("(5 + 6i) - (1 + 2i)")
        self.assertEqual(result.real, 4)
        self.assertEqual(result.im, 4)
        result = self.calc.evaluate_expression("(1 + 2i) * (3 + 4i)")
        self.assertEqual(result.real, -5)
        self.assertEqual(result.im, 10)
  
    def test_evaluate_expression_with_nested_complex_operations(self):
        result = self.calc.evaluate_expression("((1 + 1i) + (2 + 2i)) * (3 + 3i)")
        self.assertAlmostEqual(result.real, 0, places=1)
        self.assertAlmostEqual(result.im, 18, places=1)
        result = self.calc.evaluate_expression("((2 + 3i) - (1 + 1i)) * (4 + 4i)")
        self.assertAlmostEqual(result.real, -4, places=1)
        self.assertAlmostEqual(result.im, 12, places=1)
   
    def test_evaluate_expression_invalid(self):
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("2 / 0")
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("sqrt(-1)")
    

if __name__ == '__main__':
    unittest.main()
