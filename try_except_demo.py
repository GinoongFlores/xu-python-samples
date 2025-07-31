# Simple demonstration of try and except blocks in Python
# This program shows how to handle errors when converting user input to integers

def main():
    """
    Main function that demonstrates try/except blocks for handling user input errors.
    """
    print("Welcome to the Try/Except Demonstration!")
    print("This program will ask you to enter numbers and handle any input errors.")
    print("-" * 60)
    
    # Example 1: Basic try/except for integer conversion
    print("\nExample 1: Converting user input to an integer")
    try:
        # Prompt the user for input
        user_input = input("Please enter a whole number: ")
        
        # Attempt to convert the input to an integer
        number = int(user_input)
        
        # If successful, perform some operation
        result = number * 2
        print(f"Success! You entered {number}")
        print(f"Double your number is: {result}")
        
    except ValueError:
        # This block runs if the conversion to int() fails
        print("Error: That's not a valid whole number!")
        print("Please make sure you enter only digits (like 5, 123, or -7)")
    
    # Example 2: Try/except with multiple operations
    print("\n" + "-" * 60)
    print("Example 2: Multiple operations with error handling")
    
    try:
        # Get two numbers from the user
        first_input = input("Enter your first number: ")
        second_input = input("Enter your second number: ")
        
        # Convert both inputs to integers
        first_number = int(first_input)
        second_number = int(second_input)
        
        # Perform calculations
        sum_result = first_number + second_number
        difference = first_number - second_number
        
        # Display results
        print(f"\nResults:")
        print(f"{first_number} + {second_number} = {sum_result}")
        print(f"{first_number} - {second_number} = {difference}")
        
    except ValueError:
        # Handle conversion errors
        print("Error: One or both of your inputs were not valid numbers!")
        print("Please enter only whole numbers (like 10, -5, or 0)")
    
    # Example 3: Using try/except in a loop for persistent input
    print("\n" + "-" * 60)
    print("Example 3: Keep asking until we get a valid number")
    
    valid_number = None
    attempts = 0
    max_attempts = 3
    
    # Keep trying until we get a valid number or reach max attempts
    while valid_number is None and attempts < max_attempts:
        try:
            attempts += 1
            user_input = input(f"Attempt {attempts}: Enter a number between 1 and 100: ")
            
            # Try to convert to integer
            number = int(user_input)
            
            # Check if the number is in the valid range
            if 1 <= number <= 100:
                valid_number = number
                print(f"Perfect! You entered {number}")
                print(f"The square of {number} is {number ** 2}")
            else:
                print(f"The number {number} is not between 1 and 100. Try again!")
                
        except ValueError:
            print("That's not a valid number. Please try again!")
            
        # Give feedback on remaining attempts
        if valid_number is None and attempts < max_attempts:
            remaining = max_attempts - attempts
            print(f"You have {remaining} attempt(s) left.")
    
    # Final message
    if valid_number is None:
        print("\nYou've used all your attempts. Don't worry, practice makes perfect!")
    
    print("\nThanks for learning about try/except blocks!")
    print("Remember: try/except helps your program handle errors gracefully!")

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()