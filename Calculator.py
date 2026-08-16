import math


class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    # ---------------- Basic Operations ----------------

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot calculate modulus with zero.")
        return a % b

    # ---------------- Scientific Operations ----------------

    def square_root(self, number):
        if number < 0:
            raise ValueError("Square root of a negative number is not supported.")
        return math.sqrt(number)

    def factorial(self, number):
        if number < 0 or not number.is_integer():
            raise ValueError("Factorial requires a non-negative integer.")
        return math.factorial(int(number))

    def percentage(self, number, percent):
        return number * percent / 100

    def logarithm(self, number):
        if number <= 0:
            raise ValueError("Logarithm is defined only for positive numbers.")
        return math.log10(number)

    def natural_log(self, number):
        if number <= 0:
            raise ValueError("Natural logarithm is defined only for positive numbers.")
        return math.log(number)

    def sine(self, angle):
        return math.sin(math.radians(angle))

    def cosine(self, angle):
        return math.cos(math.radians(angle))

    def tangent(self, angle):
        return math.tan(math.radians(angle))

    # ---------------- History ----------------

    def add_history(self, expression, result):
        self.history.append(f"{expression} = {result}")

    def show_history(self):
        if not self.history:
            print("\nNo calculation history.")
            return

        print("\n========== HISTORY ==========")

        for index, item in enumerate(self.history, start=1):
            print(f"{index}. {item}")

    def clear_history(self):
        self.history.clear()
        print("\nHistory cleared successfully.")

    # ---------------- Memory ----------------

    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0


# ==========================================================
# Utility Functions
# ==========================================================

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_menu():
    print("\n")
    print("=" * 45)
    print("          ADVANCED PYTHON CALCULATOR")
    print("=" * 45)

    print("\n--- Basic Operations ---")
    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Power")
    print("6.  Modulus")

    print("\n--- Scientific Operations ---")
    print("7.  Square Root")
    print("8.  Factorial")
    print("9.  Percentage")
    print("10. Logarithm")
    print("11. Natural Log")
    print("12. Sine")
    print("13. Cosine")
    print("14. Tangent")

    print("\n--- Memory ---")
    print("15. Memory Add")
    print("16. Memory Subtract")
    print("17. Memory Recall")
    print("18. Memory Clear")

    print("\n--- Other ---")
    print("19. Show History")
    print("20. Clear History")
    print("21. Exit")

    print("=" * 45)


# ==========================================================
# Main Program
# ==========================================================

def main():

    calculator = Calculator()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        try:

            # ---------------- Basic Operations ----------------

            if choice == "1":

                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                result = calculator.add(a, b)

                expression = f"{a} + {b}"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "2":

                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                result = calculator.subtract(a, b)

                expression = f"{a} - {b}"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "3":

                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                result = calculator.multiply(a, b)

                expression = f"{a} * {b}"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "4":

                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")

                result = calculator.divide(a, b)

                expression = f"{a} / {b}"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "5":

                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")

                result = calculator.power(a, b)

                expression = f"{a} ^ {b}"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "6":

                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                result = calculator.modulus(a, b)

                expression = f"{a} % {b}"

                print("Result:", result)

                calculator.add_history(expression, result)

            # ---------------- Scientific Operations ----------------

            elif choice == "7":

                number = get_number("Enter number: ")

                result = calculator.square_root(number)

                expression = f"sqrt({number})"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "8":

                number = get_number("Enter number: ")

                result = calculator.factorial(number)

                expression = f"{int(number)}!"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "9":

                number = get_number("Enter number: ")
                percent = get_number("Enter percentage: ")

                result = calculator.percentage(number, percent)

                expression = f"{percent}% of {number}"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "10":

                number = get_number("Enter number: ")

                result = calculator.logarithm(number)

                expression = f"log10({number})"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "11":

                number = get_number("Enter number: ")

                result = calculator.natural_log(number)

                expression = f"ln({number})"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "12":

                angle = get_number("Enter angle in degrees: ")

                result = calculator.sine(angle)

                expression = f"sin({angle})"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "13":

                angle = get_number("Enter angle in degrees: ")

                result = calculator.cosine(angle)

                expression = f"cos({angle})"

                print("Result:", result)

                calculator.add_history(expression, result)

            elif choice == "14":

                angle = get_number("Enter angle in degrees: ")

                result = calculator.tangent(angle)

                expression = f"tan({angle})"

                print("Result:", result)

                calculator.add_history(expression, result)

            # ---------------- Memory Operations ----------------

            elif choice == "15":

                value = get_number("Enter value to add to memory: ")

                calculator.memory_add(value)

                print("Memory:", calculator.memory)

            elif choice == "16":

                value = get_number("Enter value to subtract from memory: ")

                calculator.memory_subtract(value)

                print("Memory:", calculator.memory)

            elif choice == "17":

                print("Memory value:", calculator.memory_recall())

            elif choice == "18":

                calculator.memory_clear()

                print("Memory cleared.")

            # ---------------- History ----------------

            elif choice == "19":

                calculator.show_history()

            elif choice == "20":

                calculator.clear_history()

            # ---------------- Exit ----------------

            elif choice == "21":

                print("\nThank you for using Advanced Calculator!")

                break

            else:

                print("\nInvalid choice. Please select 1-21.")

        except (ValueError, ZeroDivisionError) as error:

            print("Error:", error)

        except Exception as error:

            print("Unexpected error:", error)


if __name__ == "__main__":
    main()