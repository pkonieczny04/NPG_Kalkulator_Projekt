#Plik nagłówkowy
import math, re

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
        if isinstance(a, Complex) or isinstance(b, Complex):
            if not isinstance(a, Complex):
                a = Complex(a, 0)
            if not isinstance(b, Complex):
                b = Complex(b, 0)
            result = a.power(b)
            self._save_to_history(f"({a.real} + {a.im}i) ^ ({b.real} + {b.im}i) = ({result.real} + {result.im}i)")
            return result
        else:
            result = a ** b
            self._save_to_history(f"{a} ^ {b} = {result}")
            return result

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        result = a ** 0.5
        self._save_to_history(f"sqrt({a}) = {result}")
        return result  

    def evaluate_expression(self, expression):
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
                elif op == '+':
                    values.append(self.add(a, b))
                elif op == '-':
                    values.append(self.subtract(a, b))
                elif op == '*':
                    values.append(self.multiply(a, b))
                elif op == '/':
                    if b.real == 0 and b.im == 0:
                        raise ValueError("Cannot divide by zero")
                    values.append(self.divide(a, b))
                elif op == '^':
                    values.append(self.power(a, b))
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
                    values.append(round(a / b, 10))
                elif op == '^':
                    values.append(a ** b)
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
            elif token == 'sqrt':  
                operators.append(token)
            else:
                while (operators and precedence(operators[-1]) >= precedence(token)):
                    apply_operator(operators.pop())
                operators.append(token)
            i += 1

        while operators:
            op = operators.pop()
            if op == 'sqrt':  
                if len(values) == 0:
                    raise ValueError("Invalid expression")
                values.append(self.sqrt(values.pop()))
            else:
                apply_operator(op)

        return values[0]
        
        if isinstance(result, Complex):
            self._save_to_history(f"{expression} = {result.real} + {result.im}i")
        else:
            self._save_to_history(f"{expression} = {result}")

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


    
