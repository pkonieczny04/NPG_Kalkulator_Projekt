import unittest
from calculator import Calculator

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
