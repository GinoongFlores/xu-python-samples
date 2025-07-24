# Capture user information using input()
user_name = input("Enter your name: ")                   # String
user_age = int(input("Enter your age: "))                 # Integer
user_weight = float(input("Enter your weight (kg): "))    # Float

# Capture workout details
workout_type = input("What type of workout did you do? ")  # String
workout_duration = int(input("Enter the duration (in minutes): "))  # Integer
workout_distance = float(input("Enter the distance covered (km): "))  # Float

# Create a summary message using f-strings
profile_summary = f"Name: {user_name}, Age: {user_age}, Weight: {user_weight} kg"
workout_summary = f"Workout: {workout_type} for {workout_duration} minutes, covering {workout_distance} km"

# Optional: Using slicing to display part of the user's name
name_prefix = user_name[:3]  # First three characters of the name

# Display the results
print("\n--- User Profile ---")
print(profile_summary)
print("\n--- Workout Details ---")
print(workout_summary)
print(f"\nA quick look at your name: {name_prefix}")

# (Optional Extra Credit)
# If you want to structure your code into functions, you could create a function like:
def display_summary(name, age, weight, workout, duration, distance):
    summary = f"{name} ({age} years, {weight} kg) did {workout} for {duration} minutes covering {distance} km."
    return summary

# Then call it and explain why this modular approach could be beneficial.
display_summary()