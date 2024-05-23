#Plik nagłówkowy
import math

class Calculator:

    def __init__(self):
        self.history = []
         
    def add(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            return a.add(b)
        else:
            self._save_to_history(f"add({a}, {b}) = {a+b}")
            return a + b

    def subtract(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            return a.subtract(b)
        else:
            self._save_to_history(f"subtract({a}, {b}) = {a-b}")
            return a - b

    def multiply(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            return a.multiply(b)
        else:
            self._save_to_history(f"multiply({a}, {b}) = {a*b}")
            return a * b

    def divide(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            return a.divide(b)
        else:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            self._save_to_history(f"divide({a}, {b}) = {a/b}")
            return a / b

    def power(self, a, b):
        pass

    def sqrt(self, a):
        pass  

    
class Complex:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def add(self, other):
        return Complex(self.real + other.real, self.im + other.im)

    def subtract(self, other):
        return Complex(self.real - other.real, self.im - other.im)

    def multiply(self, other):
        real = self.real * other.real - self.im * other.im
        im = self.real * other.im + self.im * other.real
        return Complex(real, im)

    def divide(self, other):
        if other.real == 0 and other.im == 0:
            raise ValueError("Cannot divide by zero")
        denominator = other.real ** 2 + other.im ** 2
        real = (self.real * other.real + self.im * other.im) / denominator
        im = (self.im * other.real - self.real * other.im) / denominator
        return Complex(real, im)


    
