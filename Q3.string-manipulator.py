# Asking user for an Sentence and displaying :
#     1.original sentence
#     2.Total characters with spaces
#     3.Total characters without spaces
#     4.Total words
#     5.Uppercase 
#     6.Lowercase 
#     7.Title case 
#     8.Last word 
#     9.First 
#    10.Reversed 

Sentence=input("Enter an Original Sentence:") # user input as sentence
print("Original:",Sentence)                             #printing original
print("Characters(with spaces):",len(Sentence)) #printing characters with spaces
print("Characters(without spaces):",len(Sentence.replace(" ",""))) # without spaces
print("Words:",len(Sentence.split()))   #splitiing sentence into words using split sunc
print("UPPERCASE:",Sentence.upper())    #converting uppercase
print("Lowercase:",Sentence.lower())    #converting lowercase
print("Title Case:",Sentence.title())   #ritlecase
words=Sentence.split()
print("First Word:",words[0])
print("Last Word:",words[-1])
print("Reversed:",Sentence[::-1])    #reversed sentence 

# Output:1
# Enter an Original Sentence: Hello World python
# Original:  Hello World python
# CSharacters(with spaces): 19
# Characters(without spaces): 16
# Words: 3
# UPPERCASE:  HELLO WORLD PYTHON
# Lowercase:  hello world python
# Title Case:  Hello World Python
# First Word: Hello
# Last Word: python
# Reversed: nohtyp dlroW olleH

# Output:2
# Enter an Original Sentence:Hey!! Apoorva, What's Up?
# Original: Hey!! Apoorva, What's Up?
# CSharacters(with spaces): 25
# Characters(without spaces): 22
# Words: 4
# UPPERCASE: HEY!! APOORVA, WHAT'S UP?
# Lowercase: hey!! apoorva, what's up?
# Title Case: Hey!! Apoorva, What'S Up?
# First Word: Hey!!
# Last Word: Up?
# Reversed: ?pU s'tahW ,avroopA !!yeH