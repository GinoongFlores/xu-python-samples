# Integer Input Activity - Try/Except Error Handling Demonstration
# This activity demonstrates how to safely handle user input conversion to integers
# using try and except blocks to catch and handle potential errors.

def get_integer_input(prompt):
    """
    Prompts the user for input and attempts to convert it to an integer.
    Uses try/except to handle conversion errors gracefully.
    
    Args:
        prompt (str): The message to display when asking for input
        
    Returns:
        int: The converted integer value, or None if conversion fails
    """
    try:
        # Attempt to get user input and convert it to an integer
        user_input = input(prompt)
        integer_value = int(user_input)
        return integer_value
    
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print(f"Error: '{user_input}' is not a valid integer.")
        print("Please enter a whole number (e.g., 42, -15, 0)")
        return None
    
    except KeyboardInterrupt:
        # Handle the case where the user presses Ctrl+C
        print("\nOperation cancelled by user.")
        return None

def calculate_age_in_days(age_in_years):
    """
    Calculates approximate age in days based on age in years.
    
    Args:
        age_in_years (int): Age in years
        
    Returns:
        int: Approximate age in days
    """
    # Simple calculation assuming 365 days per year
    return age_in_years * 365

def main():
    """
    Main function that demonstrates try/except error handling with user input.
    This activity asks the user for their age and calculates their age in days.
    """
    print("=== Integer Input Activity ===")
    print("This program will ask for your age and calculate your age in days.")
    print("It demonstrates how to handle errors when converting user input to integers.\n")
    
    # Main program loop - continues until valid input is received or user quits
    while True:
        try:
            # Ask user for their age using our error-handling function
            print("Enter your age in years (or 'quit' to exit):")
            
            # Get user input first to check for quit command
            user_input = input("Age: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thank you for using the Integer Input Activity!")
                break
            
            # Try to convert the input to an integer
            age = int(user_input)
            
            # Validate that the age makes sense
            if age < 0:
                print("Error: Age cannot be negative. Please enter a positive number.")
                continue
            elif age > 150:
                print("Error: Age seems unrealistic. Please enter a reasonable age.")
                continue
            
            # If we get here, the input is valid
            days = calculate_age_in_days(age)
            print(f"\nGreat! You are approximately {days:,} days old.")
            
            # Ask if user wants to try again
            try_again = input("\nWould you like to try with another age? (y/n): ").strip().lower()
            if try_again not in ['y', 'yes']:
                print("Thank you for using the Integer Input Activity!")
                break
                
        except ValueError:
            # Handle the case where int() conversion fails
            print(f"Error: '{user_input}' is not a valid integer.")
            print("Please enter a whole number for your age.\n")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nOperation cancelled by user.")
            print("Thank you for using the Integer Input Activity!")
            break
            
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            print("Please try again.\n")

# Entry point - runs the main function when script is executed directly
if __name__ == "__main__":
    main()