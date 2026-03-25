

# # Create a calculator using functions. 
# Required Functions: 
# 1.	add(a, b)   
# 2.	subtract(a, b) 
# 3.	multiply(a, b)   
# 4.	divide(a, b) - handle division by zero   
# 5.	modulus(a, b)   
# 6.	power(a, b)   
# 7.	calculator() - main function with menu 
 
# The calculator() function should display a menu, take user input, call the appropriate function, and display the result. Include an Exit option. 


def add(a, b):
    return a + b

def subtract(a, b): # defining each operations using funtions like add ,subtarct,multiply, divide ,modulus and power
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return " Division by zero is not allowed!"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


def calculator():                            # using main function called calculator to perform them
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ") #taking user input for choice

        if choice == "7":
            print("Exiting Calculator... 👋")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                a = float(input("Enter first number: "))          # user input for a and b 
                b = float(input("Enter second number: "))
               
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
                if choice == "1":
                 print("Result:", add(a, b))             #calculating add 

                elif choice == "2":                        
                 print("Result:", subtract(a, b))        ##calculating subtract if choice is 2

                elif choice == "3":
                  print("Result:", multiply(a, b))          ##calculating multiply if choice is 3

                elif choice == "4":
                  print("Result:", divide(a, b))           ##calculating divide if choice is 4

                elif choice == "5":
                  print("Result:", modulus(a, b))         ##calculating modulus if choice is 5

                elif choice == "6":
                 print("Result:", power(a, b))               ##calculating power if choice is 6

        else:
            print("Invalid choice! Please select between 1 and 7.")

calculator()



# output 1:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus
# 6. Power
# 7. Exit
# Enter your choice (1-7): 1
# Enter first number: 6
# Enter second number: 7
# Result: 13.0


# output 2:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus
# 6. Power
# 7. Exit
# Enter your choice (1-7): 4
# Enter first number:  3
# Enter second number: 4
# Result: 0.75