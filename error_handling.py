def divide_numbers(a, b):
    """Divides two numbers and handles division by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Execution of divide_numbers is complete.")

def main():
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform division and print the result
        result = divide_numbers(num1, num2)
        if result is not None:
            print(f"The result of dividing {num1} by {num2} is {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()