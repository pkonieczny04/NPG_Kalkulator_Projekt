#Plik nagłówkowy
import math

class Calculator:

    def __init__(self):
        self.history = []

    def _save_to_history(self, operation):
        if len(self.history) < 10:
            self.history.append(operation)
        else:
            self.history.pop(0)
            self.history.append(operation)
            

    def get_history(self):
        for i in self.history:
            print(i)

    def clear_history(self):
        self.history.clear()
         
    def add(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            result = a.add(b)
            self._save_to_history(f"({a.real} + {a.im}i) + ({b.real} + {b.im}i) = ({result.real} + {result.im}i)")
            return result
        else:
            self._save_to_history(f"{a} + {b} = {a+b}")
            return a + b

    def subtract(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            result = a.subtract(b)
            self._save_to_history(f"({a.real} + {a.im}i) - ({b.real} + {b.im}i) = ({result.real} + {result.im}i)")
            return result
        else:
            self._save_to_history(f"{a} - {b} = {a-b}")
            return a - b

    def multiply(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            result = a.multiply(b)
            self._save_to_history(f"({a.real} + {a.im}i) * ({b.real} + {b.im}i) = ({result.real} + {result.im}i)")
            return result
        else:
            self._save_to_history(f"{a} * {b} = {a*b}")
            return a * b

    def divide(self, a, b):
        if isinstance(a, Complex) and isinstance(b, Complex):
            result = a.divide(b)
            self._save_to_history(f"({a.real} + {a.im}i) / ({b.real} + {b.im}i) = ({result.real} + {result.im}i)")
            return result
        else:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            self._save_to_history(f"{a} / {b} = {a/b}")
            return a / b

    def power(self, a, b):
        result = a ** b
        self._save_to_history(f"{a} ^ {b} = {result}")
        return result

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        result = a ** 0.5
        self._save_to_history(f"sqrt({a}) = {result}")
        return result  

    
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


    
