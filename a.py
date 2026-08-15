class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

class ScientificCalculator(Calculator):
    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return a ** 0.5

if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(5, 3))
    print("Subtraction:", calc.subtract(5, 3))
    print("Multiplication:", calc.multiply(5, 3))
    print("Division:", calc.divide(5, 3))
    sci_calc = ScientificCalculator()
    print("Power:", sci_calc.power(2, 3))
    print("Square Root:", sci_calc.square_root(16))
    print("Square Root of negative number:", sci_calc.square_root(-4))  # This will raise an error

