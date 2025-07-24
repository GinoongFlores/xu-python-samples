# Function to find the longest word in a sentence
def find_longest_word(sentence):
    """Returns the longest word in the given sentence."""
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Main function to run the program
def main():
    try:
        sentence = input("Enter a sentence: ")

        # Remove extra whitespace and convert to lowercase
        cleaned_sentence = ' '.join(sentence.split()).lower()

        # Find the longest word
        longest_word = find_longest_word(cleaned_sentence)

        # Print the longest word
        print(f"The longest word is: '{longest_word}'")

    except Exception as e:
        print("An error occurred while processing the input:", e)

if __name__ == "__main__":
    main()