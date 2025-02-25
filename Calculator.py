import math

class Calculator:
    def add(self, a, b):
        # Adds two numbers and returns the result
        return a + b
    
    def subtract(self, a, b):
        # Subtracts the second number from the first and returns the result
        return a - b
    
    def multiply(self, a, b):
        # Multiplies two numbers and returns the result
        return a * b
    
    def divide(self, a, b):
        # Divides the first number by the second
        # Returns an error message if the second number is zero
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
        
    def square_root(self, x):
        # Returns the square root of the given number
        # Raises ValueError if the input is negative
        if x < 0:
            return "Error: Cannot compute square root of a negative number."
        return math.sqrt(x)


if __name__ == "__main__":
    calculator = Calculator()

    num1 = 16
    num2 = 4
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")

