
"""
Project 01: Simple Calculator
Author: Naksala Sabeenthiran
Description: A command-line calculator using Python.
"""


# Function to display calculator menu
def display_menu():
    print("\n================================")
    print("       SIMPLE CALCULATOR")
    print("================================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. View Calculation History")
    print("8. Exit")
    print("================================")


# Function to get valid number input
def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to perform calculations
def calculate(num1, num2, choice):

    if choice == "1":
        return num1 + num2, "+"

    elif choice == "2":
        return num1 - num2, "-"

    elif choice == "3":
        return num1 * num2, "*"

    elif choice == "4":
        if num2 == 0:
            raise ZeroDivisionError(
                "Cannot divide by zero!"
            )
        return num1 / num2, "/"

    elif choice == "5":
        if num2 == 0:
            raise ZeroDivisionError(
                "Cannot calculate modulus with zero!"
            )
        return num1 % num2, "%"

    elif choice == "6":
        if num1 == 0 and num2 < 0:
            raise ZeroDivisionError(
                "Zero cannot have a negative exponent!"
            )
        result = num1 ** num2
        if isinstance(result, complex):
            raise ValueError(
                "Complex number results are not supported!"
            )
        return result, "**"


# Function to display calculation history
def show_history(history):

    print("\n===== CALCULATION HISTORY =====")

    if not history:
        print("No calculations yet.")
    else:
        for index, calculation in enumerate(
            history, start=1
        ):
            print(f"{index}. {calculation}")


# Main program
def main():

    history = []

    print("Welcome to Python Simple Calculator!")

    while True:

        display_menu()

        choice = input(
            "Enter your choice (1-8): "
        ).strip()

        # Exit program
        if choice == "8":
            print("\nThank you for using the calculator!")
            print("Goodbye!")
            break

        # View history
        elif choice == "7":
            show_history(history)
            continue

        # Validate menu choice
        elif choice not in (
            "1", "2", "3", "4", "5", "6"
        ):
            print("Invalid choice! Please try again.")
            continue

        # Get numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result, operator = calculate(
                num1, num2, choice
            )

            # Format calculation result
            calculation = (
                f"{num1:g} {operator} {num2:g}"
                f" = {result:g}"
            )

            print("\nResult:", calculation)

            # Save calculation history
            history.append(calculation)

        except (ZeroDivisionError, ValueError, OverflowError) as error:
            print("\nError:", error)

    print("\nProgram ended successfully.")


# Entry point
if __name__ == "__main__":
    main()