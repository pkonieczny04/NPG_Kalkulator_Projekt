import unittest
from calculator import Calculator, Complex

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Inicjalizacja obiektu Calculator przed każdym testem
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 5), 4) # -1 + 5 = 4
    
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(self.calc.subtract(10, 7), 3) # 10 - 7 = 3
        self.assertEqual(self.calc.subtract(3, 4) , -1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 6), 24)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(-5, -2), 10)


    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)      # 2 ** 3 = 8
        self.assertEqual(self.calc.power(4, 0.5), 2)    # 4 ** 0.5 = 2 (pierwiastek kwadratowy)
        self.assertEqual(self.calc.power(4, 2), 16)
    
    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(25), 5)         # sqrt(25) = 5
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)  # Nie można obliczyć pierwiastka z liczby ujemnej

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
        self.assertEqual(len(self.history), 1)
        self.assertEqual(self.get_history, "2 + 3 = 5")
        self.clear_history

    def test_subtract_to_history(self):
        a = 5
        b = 3
        result = self.calc.subtract(a, b)
        self.assertEqual(len(self.history), 1)
        self.assertEqual(self.get_history, "5 - 3 = 2")
        self.clear_history

    def test_multiply_to_history(self):
        a = 5
        b = 6
        result = self.calc.multiply(a, b)
        self.assertEqual(len(self.history), 1)
        self.assertEqual(self.get_history, "5 * 6 = 30")
        self.clear_history

    def test_divide_to_history(self):
        a = 10
        b = 2
        result = self.calc.divide(a, b)
        self.assertEqual(len(self.history), 1)
        self.assertEqual(self.get_history, "10 / 2 = 5")
        self.clear_history

    def test_power_to_history(self):
        a = 2
        b = 10
        result = self.calc.power(a, b)
        self.assertEqual(len(self.history), 1)
        self.assertEqual(self.get_history, "2 ^ 10 = 1024")
        self.clear_history

    def test_sqrt_to_history(self):
        a = 16
        result = self.calc.sqrt(a)
        self.assertEqual(len(self.history), 1)
        self.assertEqual(self.get_history, "sqrt(a) = 4")
        self.clear_history

    def test_add_complex_to_history(self):
            a = Complex(1, 2)
            b = Complex(3, 4)
            result = self.calc.add(a, b)
            self.assertEqual(len(self.history), 1)
            self.assertEqual(self.get_history, "(1 + 2i) + (3 + 4i) = (4 + 6i)")
            self.clear_history

    def test_subtract_complex_to_history(self):
            a = Complex(5, 3)
            b = Complex(2, 1)
            result = self.calc.subtract(a, b)
            self.assertEqual(len(self.history), 1)
            self.assertEqual(self.get_history, "(5 + 3i) - (2 + 1i) = (3 + 2i)")
            self.clear_history

    def test_multiply_complex_to_history(self):
            a = Complex(2, 3)
            b = Complex(4, 5)
            result = self.calc.multiply(a, b)
            self.assertEqual(len(self.history), 1)
            self.assertEqual(self.get_history, "(2 + 3i) * (4 + 5i) = (-7 + 22i)")
            self.clear_history

    def test_divide_complex_to_history(self):
            a = Complex(1, 8)
            b = Complex(2, 3)
            result = self.calc.divide(a, b)
            self.assertEqual(len(self.history), 1)
            self.assertEqual(self.get_history, "(1 + 8i) / (2 + 3i) = (2 + 1i)")
            self.clear_history

    def test_history_clearing(self):
        result = self.calc.add(1, 1)
        self.assertEqual(len(self.history), 1)
        self.clear_history
        self.assertEqual(len(self.history), None)

    def test_history_max_10_elements(self):
        for i in range (0, 15):
            result = self.calc.add(1, 1)
        self.assertEqual(len(self.history, 10)
        self.clear_history
    

if __name__ == '__main__':
    unittest.main()


