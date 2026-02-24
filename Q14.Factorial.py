# Program to calculate factorial with step-by-step display

num = int(input("Enter a number: "))   # Take user input
if num < 0:
    print("Factorial is not defined for negative numbers.")

elif num == 0:
    print("0! = 1")    # factorial of 0 is 1

else:
    factorial = 1      # Variable to store factorial result
    
    print(f"{num}! = ", end="")   # Print beginning part 
    
    for i in range(num, 0, -1):   # Loop from num down to 1
        factorial *= i            # Multiply factorial by current number
        
        print(i, end="")          # Print the number
        
        if i != 1:                
            print(" × ", end="")
    
    print(" =", factorial)        # Printing


#output 1:
#Enter a number:  4
#4! = 4 × 3 × 2 × 1 = 24


#output 2:
#Enter a number:  6
#6! = 6 × 5 × 4 × 3 × 2 × 1 = 720