import math
import re

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

    def add(self, a, b, save_history=True):
        if isinstance(a, Complex) or isinstance(b, Complex):
            if not isinstance(a, Complex):
                a = Complex(a, 0)
            if not isinstance(b, Complex):
                b = Complex(b, 0)
            result = a.add(b)
            if save_history:
                self._save_to_history(f"({a}) + ({b}) = {result}")
            return result
        else:
            result = a + b
            if save_history:
                self._save_to_history(f"{a} + {b} = {result}")
            return result

    def subtract(self, a, b, save_history=True):
        if isinstance(a, Complex) or isinstance(b, Complex):
            if not isinstance(a, Complex):
                a = Complex(a, 0)
            if not isinstance(b, Complex):
                b = Complex(b, 0)
            result = a.subtract(b)
            if save_history:
                self._save_to_history(f"({a}) - ({b}) = {result}")
            return result
        else:
            result = a - b
            if save_history:
                self._save_to_history(f"{a} - {b} = {result}")
            return result

    def multiply(self, a, b, save_history=True):
        if isinstance(a, Complex) or isinstance(b, Complex):
            if not isinstance(a, Complex):
                a = Complex(a, 0)
            if not isinstance(b, Complex):
                b = Complex(b, 0)
            result = a.multiply(b)
            if save_history:
                self._save_to_history(f"({a}) * ({b}) = {result}")
            return result
        else:
            result = a * b
            if save_history:
                self._save_to_history(f"{a} * {b} = {result}")
            return result

    def divide(self, a, b, save_history=True):
        if isinstance(a, Complex) or isinstance(b, Complex):
            if not isinstance(a, Complex):
                a = Complex(a, 0)
            if not isinstance(b, Complex):
                b = Complex(b, 0)
            result = a.divide(b)
            if save_history:
                self._save_to_history(f"({a}) / ({b}) = {result}")
            return result
        else:
            if b == 0:
                raise ValueError("Cannot divide by zero")
            result = a / b
            if save_history:
                self._save_to_history(f"{a} / {b} = {result}")
            return result

    def power(self, a, b, save_history=True):
        if isinstance(a, Complex) or isinstance(b, Complex):
            if not isinstance(a, Complex):
                a = Complex(a, 0)
            if not isinstance(b, Complex):
                b = Complex(b, 0)
            result = a.power(b)
            if save_history:
                self._save_to_history(f"({a}) ^ ({b}) = {result}")
            return result
        else:
            result = round(a ** b, 10)
            if save_history:
                self._save_to_history(f"{a} ^ {b} = {result}")
            return result

    def sqrt(self, a, save_history=True):
        if isinstance(a, Complex):
            result = a.sqrt()
            if save_history:
                self._save_to_history(f"sqrt({a}) = {result}")
            return result
        else:
            if a < 0:
                raise ValueError("Cannot take the square root of a negative number")
            result = round(math.sqrt(a), 10)
            if save_history:
                self._save_to_history(f"sqrt({a}) = {result}")
            return result

    def evaluate_expression(self, expression):
        original_expression = expression
        expression = expression.replace(' ', '')
        tokens = re.findall(r'\d+\.?\d*|\+|\-|\*|\/|\^|\(|\)|i', expression)

        values = []
        operators = []

        def apply_operator(op):
            if len(values) < 2:
                raise ValueError("Invalid expression")
            
            b = values.pop()
            a = values.pop()
        
            if isinstance(a, Complex) or isinstance(b, Complex):
                if not isinstance(a, Complex):
                    a = Complex(a, 0)
                if not isinstance(b, Complex):
                    b = Complex(b, 0)
                if op == '+':
                    values.append(self.add(a, b, save_history=False))
                elif op == '-':
                    values.append(self.subtract(a, b, save_history=False))
                elif op == '*':
                    values.append(self.multiply(a, b, save_history=False))
                elif op == '/':
                    values.append(self.divide(a, b, save_history=False))
                elif op == '^':
                    values.append(self.power(a, b, save_history=False))
            else:
                if op == '+':
                    values.append(a + b)
                elif op == '-':
                    values.append(a - b)
                elif op == '*':
                    values.append(a * b)
                elif op == '/':
                    if b == 0:
                        raise ValueError("Cannot divide by zero")
                    values.append(a / b)
                elif op == '^':
                    values.append(round(a ** b, 10))

        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            if op == '^':
                return 3
            return 0

        i = 0
        while i < len(tokens):
            token = tokens[i]

            if re.match(r'\d+\.?\d*', token):
                if i + 1 < len(tokens) and tokens[i + 1] == 'i':
                    values.append(Complex(0, float(token)))
                    i += 1
                else:
                    values.append(float(token))
            elif token == 'i':
                if len(values) == 0 or isinstance(values[-1], Complex):
                    values.append(Complex(0, 1))
                else:
                    values[-1] = Complex(0, values.pop())
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators.pop())
                operators.pop()
            else:
                while (operators and precedence(operators[-1]) >= precedence(token)):
                    apply_operator(operators.pop())
                operators.append(token)
            i += 1

        while operators:
            apply_operator(operators.pop())

        result = values[0]
        result_str = self._format_result(result)
        self._save_to_history(f"{original_expression} = {result_str}")

        return result

    def _format_result(self, result):
        if isinstance(result, Complex):
            return str(result)
        else:
            return str(result)


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
        if isinstance(other, Complex):
            if other.real == 0 and other.im == 0:
                raise ValueError("Cannot divide by zero")
            denominator = other.real ** 2 + other.im ** 2
            real = (self.real * other.real + self.im * other.im) / denominator
            im = (self.im * other.real - self.real * other.im) / denominator
        else:
            if other == 0:
                raise ValueError("Cannot divide by zero")
            real = self.real / other
            im = self.im / other
        return Complex(round(real, 10), round(im, 10))
    
    def power(self, other):
        if other.real == 0 and other.im == 0:
            return Complex(1, 0)
        elif self.real == 0 and self.im == 0:
            return Complex(0, 0)
        else:
            c = complex(self.real, self.im) ** complex(other.real, other.im)
            return Complex(round(c.real, 10), round(c.imag, 10))

    def sqrt(self):
        c = complex(self.real, self.im)
        result = c ** 0.5
        return Complex(round(result.real, 10), round(result.imag, 10))

    def __repr__(self):
        return f"{self.real} + {self.im}i" if self.im >= 0 else f"{self.real} - {-self.im}i"

    def __str__(self):
        return self.__repr__()
