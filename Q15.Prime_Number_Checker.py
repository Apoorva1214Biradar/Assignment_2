# Part 1: Check if a single number is prime

num = int(input("Enter a number: "))
if num < 2:
    print(num, "is NOT a prime number.")
elif num == 2:
    print("2 is a PRIME number.")

else:
    is_prime = True   # Assume number is prime
    
    for i in range(2, int(num ** 0.5) + 1):   # Check till square root
        if num % i == 0:                      # If divisible
            is_prime = False
            break                             # Stop loop immediately
    
    if is_prime:
        print(num, "is a PRIME number.")
    else:
        print(num, "is NOT a prime number.")


# Part 2: Prime numbers in a given range

start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for num in range(start, end + 1):
    
    if num < 2:
        continue   # Skip numbers less than 2
    
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=", ")


#output 1:
# Enter a number: 3
# 3 is a PRIME number.
# Enter start range:  2
# Enter end range: 5
# Prime numbers: 2, 3, 5, 



#output 2:
# Enter a number: 10
# 10 is NOT a prime number.
# Enter start range: 3
# Enter end range: 5
# Prime numbers: 3, 5, 