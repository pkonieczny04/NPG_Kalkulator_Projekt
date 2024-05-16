#Plik nagłówkowy
import math

class Calculator:
    def __init__(self):
        self.history = []

    def addition(self, a, b) :
        result = a + b
        self._save_to_history(f"add({a}, {b}) = {result}")
        return result

    def substract(self, a, b):
        result = a - b
        self._save_to_history(f"subtract({a}, {b}) = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self._save_to_history(f"multiply({a}, {b}) = {result}")
        return result
    def divide(self, a, b):
        pass
    def power(self, a, b):
        pass

    def sqrt(self, a):
        pass

    
    
