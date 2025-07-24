import string

# Function to check if a word has an even or odd length
def is_even_length(word):
    """Returns 'even' if the word's length is even, otherwise returns 'odd'."""
    return "even" if len(word) % 2 == 0 else "odd"

# Function to clean and prepare the sentence for palindrome checking
def clean_sentence(sentence):
    """Removes extra whitespace, punctuation, and converts to lowercase."""
    cleaned_sentence = ' '.join(sentence.split()).lower()
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = cleaned_sentence.translate(translator)
    return sentence_no_punct.replace(" ", "")

# Function to check if a sentence is a palindrome
def is_palindrome(sentence):
    """Checks if the given sentence is a palindrome."""
    cleaned = clean_sentence(sentence)
    return cleaned == cleaned[::-1]

# Main function to run the program
def main():
    try:
        sentence = input("Enter a sentence: ")

        if is_palindrome(sentence):
            print("The sentence is a palindrome.")
        else:
            print("The sentence is not a palindrome.")

        # Count the occurrences of each word in the sentence
        cleaned_sentence = ' '.join(sentence.split()).lower()
        word_list = cleaned_sentence.split()
        word_counts = {}
        for word in word_list:
            word_counts[word] = word_counts.get(word, 0) + 1

        # Iterate over the dictionary and print each word along with whether its length is even or odd
        print("\nWord Occurrences and Length Parity:")
        for word, count in word_counts.items():
            parity = is_even_length(word)
            print(f"'{word}': occurs {count} time(s), length is {parity}.")

    except Exception as e:
        print("An error occurred while processing the input:", e)


main()