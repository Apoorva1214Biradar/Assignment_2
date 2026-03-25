# Create the following text analysis functions: 
# 1.	count_words(text) - return number of words 
# 2.	count_vowels(text) - return number of vowels 
# 3.	count_consonants(text) - return number of consonants 
# 4.	reverse_text(text) - return reversed text 
# 5.	is_palindrome(text) - return True/False 
# 6.	remove_vowels(text) - return text without vowels 
# 7.	word_frequency(text) - return dictionary of word counts 
# 8.	longest_word(text) - return longest word 
# 9.	analyze_text(text) - calls all above functions and displays results 


def count_words(text):
    words = text.split()          # Split text into words using space
    return len(words)             # Return number of words


def count_vowels(text):
    count = 0                     # Initialize vowel counter
    for ch in text.lower():       # Convert text to lowercase and iterate
        if ch in "aeiou":         # Check if character is a vowel
            count += 1            # Increase vowel count
    return count                  # Return total vowels

def count_consonants(text):
    count = 0                                  # Initialize consonant counter
    for ch in text.lower():                     # Convert to lowercase
        if ch.isalpha() and ch not in "aeiou":  # Check alphabet but not vowel
            count += 1                          # Increase consonant count
    return count                                # Return total consonants

def reverse_text(text):
    return text[::-1]            # Reverse string using slicing

def is_palindrome(text):
    processed = text.lower()     # Convert to lowercase for case-insensitive check
    return processed == processed[::-1]   # Compare with reversed version

def remove_vowels(text):
    result = ""                  # Empty string to store result
    for ch in text:
        if ch.lower() not in "aeiou":   # Keep only non-vowel characters
            result += ch
    return result                # Return text without vowels

def word_frequency(text):
    words = text.lower().split()   # Convert to lowercase and split into words
    freq = {}                     # Create empty dictionary

    for word in words:            # Loop through words
        if word in freq:
            freq[word] += 1       # Increase count if word exists
        else:
            freq[word] = 1        # Add word to dictionary with count 1

    return freq                   # Return dictionary

def longest_word(text):
    words = text.split()                 # Split into words
    longest = max(words, key=len)        # Find word with maximum length
    return longest, len(longest)         # Return word and its length

def analyze_text(text):
    print("Words:", count_words(text))                 # Call count_words
    print("Vowels:", count_vowels(text))               # Call count_vowels
    print("Consonants:", count_consonants(text))       # Call count_consonants
    print("Reversed:", reverse_text(text))             # Call reverse_text
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")  # Call is_palindrome
    print("Without vowels:", remove_vowels(text))      # Call remove_vowels

    word, length = longest_word(text)                  # Get longest word
    print(f"Longest word: {word} ({length} letters)")

    freq = word_frequency(text)                        # Get word frequency
    print("Word Frequency:", end=" ")
    for key, value in freq.items():
        print(f"{key}: {value}", end=", ")


text = input("Enter text: ")     # Take input from user
analyze_text(text)               # Call function

# output 1:
# Enter text: "hey!! jasmine How are you doing!?"
# Words: 6
# Vowels: 11
# Consonants: 13
# Reversed: "?!gniod uoy era woH enimsaj !!yeh"
# Palindrome: No
# Without vowels: "hy!! jsmn Hw r y dng!?"
# Longest word: doing!?" (8 letters)
# Word Frequency: "hey!!: 1, jasmine: 1, how: 1, are: 1, you: 1, doing!?": 1,



# output 2:
# Enter text: This ia an Python programmnig
# Words: 5
# Vowels: 8
# Consonants: 17
# Reversed: ginmmargorp nohtyP na ai sihT
# Palindrome: No
# Without vowels: Ths  n Pythn prgrmmng
# Longest word: programmnig (11 letters)
# Word Frequency: this: 1, ia: 1, an: 1, python: 1, programmnig: 1,