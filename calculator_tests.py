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

if __name__ == '__main__':
    unittest.main()


