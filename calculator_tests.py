import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Inicjalizacja obiektu Calculator przed każdym testem
        self.calc = Calculator()
    
    def test_add(self):
        pass
    
    def test_subtract(self):
        pass
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 6), 24)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(-5, -2), 10)