# Palindrome Checker Program

text = input("Enter word/number: ")   # Take input from user

original = text                      # Store original input
processed = text.lower()             # Convert to lowercase 

reversed_text = processed[::-1]      # Reversing the input 

print("Original:", original)
print("Lowercase:", processed)
print("Reversed:", reversed_text)


if processed == reversed_text: 
    print("Result: PALINDROME")  #checkig condition for determining palindrome or not using if and else 
else:
    print("Result: NOT PALINDROME")

    
# output 1:
# Enter word/number: kannada
# Original: kannada
# Lowercase: kannada
# Reversed: adannak
# Result: NOT PALINDROME



# output 2:
# Enter word/number: SUS 
# Original: SUS
# Lowercase: sus
# Reversed: sus
# Result: PALINDROME

