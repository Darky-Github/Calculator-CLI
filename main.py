import math
import operator
import re

class CLICalculator:
    def __init__(self):
        self.basic_operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            '%': operator.mod,
        }

        self.scientific_operations = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'factorial': math.factorial,
            'abs': abs,
            'exp': math.exp,
            'deg': math.degrees,
            'rad': math.radians,
        }

    def evaluate(self, expression):
        try:
            # Handling scientific functions
            for func in self.scientific_operations:
                if func in expression:
                    expression = re.sub(
                        rf"{func}\(([^()]+)\)",
                        lambda m: str(self.scientific_operations[func](float(self.evaluate(m.group(1))))),
                        expression
                    )
            
            # Handle basic operations
            result = eval(expression, {"__builtins__": {}}, self.basic_operations)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def start(self):
        print("Python CLI Calculator - Samsung Style")
        print("Supports: Basic operations (+, -, *, /, **, %)")
        print("Scientific operations: sin, cos, tan, log, ln, sqrt, factorial, abs, exp, deg, rad")
        print("Type 'exit' to quit.")

        while True:
            user_input = input("\nEnter expression: ")
            if user_input.lower() == 'exit':
                break
            result = self.evaluate(user_input)
            print(f"Result: {result}")

if __name__ == "__main__":
    calculator = CLICalculator()
    calculator.start()
