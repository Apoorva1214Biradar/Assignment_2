# Ask the user how many numbers they want to add. Then take that many numbers as input using a loop. 
# Calculate: 1. Sum  2. Average  3. Maximum number  4. Minimum number 

# Program to calculate Sum, Average, Maximum and Minimum

from numpy import number


count = int(input("How many numbers? "))   # Ask user how many numbers they want to enter

total = 0          # Variable to store sum
maximum = None     # Variable to store maximum value
minimum = None     # Variable to store minimum value

for i in range(1, count + 1):              # Loop runs 'count' times
    num = int(input(f"Enter number {i}: "))  # Take number input
    
    total += num        # Add number to total (total = total + num)
    
    if maximum is None or num > maximum:
        maximum = num
  
    if minimum is None or num < minimum:
        minimum = num

average = total / count

# Display results
print("\nResults:")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)

#output 1:
# Enter number 1: 3
# Enter number 2: 4
# Enter number 3: 5
# Enter number 4: 5

# Results:
# Sum: 17
# Average: 4.25
# Maximum: 5
# Minimum: 3


#output 2:
# How many numbers? 4
# Enter number 1: 56
# Enter number 2: 69
# Enter number 3: 81
# Enter number 4: 88

# Results:
# Sum: 294
# Average: 73.5
# Maximum: 88
# Minimum: 56