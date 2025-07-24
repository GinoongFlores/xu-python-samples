# Mathematical Operations Toolkit - Demonstrating Loops and Functions
# This activity showcases various types of loops and function implementations

def calculate_factorial(number):
    """Calculate the factorial of a number using a for loop."""
    if number < 0:
        return None
    
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


def generate_fibonacci(count):
    """Generate a Fibonacci sequence up to count numbers using a while loop."""
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    fibonacci_sequence = [0, 1]
    current_count = 2
    
    while current_count < count:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
        current_count += 1
    
    return fibonacci_sequence


def is_prime(number):
    """Check if a number is prime using a for loop."""
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """Find all prime numbers in a given range using nested loops."""
    prime_numbers = []
    
    for number in range(start, end + 1):
        if is_prime(number):
            prime_numbers.append(number)
    
    return prime_numbers


def calculate_sum_of_digits(number):
    """Calculate the sum of digits in a number using a while loop."""
    total = 0
    number = abs(number)  # Handle negative numbers
    
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    
    return total


def create_multiplication_table(number, limit=10):
    """Create a multiplication table using a for loop."""
    print(f"\nMultiplication Table for {number}:")
    print("-" * 30)
    
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i:2d} = {result:3d}")


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("         MATHEMATICAL OPERATIONS TOOLKIT")
    print("=" * 50)
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Sequence")
    print("3. Check if Number is Prime")
    print("4. Find Prime Numbers in Range")
    print("5. Calculate Sum of Digits")
    print("6. Display Multiplication Table")
    print("7. Exit")
    print("-" * 50)


def get_positive_integer(prompt):
    """Get a positive integer from user with validation using a while loop."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_integer(prompt):
    """Get any integer from user with validation using a while loop."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """Main function to run the Mathematical Operations Toolkit."""
    print("Welcome to the Mathematical Operations Toolkit!")
    print("This program demonstrates various loops and functions in Python.")
    
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                # Factorial calculation
                number = get_positive_integer("Enter a number to calculate its factorial: ")
                result = calculate_factorial(number)
                if result is not None:
                    print(f"The factorial of {number} is: {result}")
                else:
                    print("Factorial is not defined for negative numbers.")
            
            elif choice == '2':
                # Fibonacci sequence generation
                count = get_positive_integer("Enter how many Fibonacci numbers to generate: ")
                if count == 0:
                    print("No numbers to generate.")
                else:
                    sequence = generate_fibonacci(count)
                    print(f"First {count} Fibonacci numbers: {sequence}")
            
            elif choice == '3':
                # Prime number check
                number = get_positive_integer("Enter a number to check if it's prime: ")
                if is_prime(number):
                    print(f"{number} is a prime number.")
                else:
                    print(f"{number} is not a prime number.")
            
            elif choice == '4':
                # Find primes in range
                start = get_positive_integer("Enter the start of the range: ")
                end = get_positive_integer("Enter the end of the range: ")
                if start > end:
                    print("Start value should be less than or equal to end value.")
                else:
                    primes = find_primes_in_range(start, end)
                    if primes:
                        print(f"Prime numbers between {start} and {end}: {primes}")
                    else:
                        print(f"No prime numbers found between {start} and {end}.")
            
            elif choice == '5':
                # Sum of digits
                number = get_integer("Enter a number to calculate sum of its digits: ")
                digit_sum = calculate_sum_of_digits(number)
                print(f"The sum of digits in {abs(number)} is: {digit_sum}")
            
            elif choice == '6':
                # Multiplication table
                number = get_integer("Enter a number for multiplication table: ")
                limit = get_positive_integer("Enter the limit for the table (default 10): ")
                if limit == 0:
                    limit = 10
                create_multiplication_table(number, limit)
            
            elif choice == '7':
                print("Thank you for using the Mathematical Operations Toolkit!")
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a number between 1 and 7.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()