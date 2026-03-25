 
# Create the following mathematical functions: 
# 1.	factorial(n) - return n! 
# 2.	is_prime(n) - return True if prime 
# 3.	fibonacci(n) - return nth Fibonacci number 
# 4.	sum_of_digits(n) - return sum of digits 
# 5.	reverse_number(n) - return number reversed 
# 6.	is_armstrong(n) - check if Armstrong number (e.g., 153 = 1³ + 5³ + 3³) 
# 7.	gcd(a, b) - greatest common divisor 
# 8.	lcm(a, b) - least common multiple 
# 9.	is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3) 
# 10.	math_menu() - menu to test all functions 
# Each function should be callable individually from the menu with appropriate user input. 


# 1. Factorial Function
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1): 
        result *= i
    return result


# 2. Prime Check Function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Fibonacci Function (nth Fibonacci number)
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


# 4. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


# 5. Reverse Number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


# 6. Armstrong Number Check
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n


# 7. GCD Function
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 8. LCM Function
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# 9. Perfect Number Check
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n


# 10. Menu Function
def math_menu():
    while True:

        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Prime:" if is_prime(n) else "Not Prime")

        elif choice == "3":
            n = int(input("Enter position: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Armstrong Number" if is_armstrong(n) else "Not Armstrong")

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect Number" if is_perfect_number(n) else "Not Perfect")

        elif choice == "10":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")



math_menu()