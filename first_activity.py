# Function to check if a number is even
def is_even(number):
    """Returns True if the number is even, otherwise returns False."""
    return number % 2 == 0

# Main function to run the program
def main():
    try:
        # Prompt the user to enter their name
        name = input("Enter your name: ")

        # Greet the user based on their name
        if name.lower() == "admin":
            print("Welcome, Admin!")
        else:
            print(f"Hello, {name}!")

        # Continuously ask for a valid number
        while True:
            try:
                # Prompt the user to enter a number
                number = int(input("Enter a number: "))

                # Check if the number is even or odd
                if is_even(number):
                    print("The number is even.")
                else:
                    print("The number is odd.")
                break  # Exit the loop if a valid number is entered

            except ValueError:
                # Handle invalid input by printing an error message and asking the user to try again
                print("Invalid input. Please enter a valid number.")

    except Exception as e:
        # Handle any unexpected errors by printing an error message
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()