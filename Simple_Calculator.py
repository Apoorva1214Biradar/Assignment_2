#Simple Calculator Program to display addition, subtraction, multiplication, division, modulus and exponentiation of two numbers.
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
print(f"{a} + {b} =",a+b)
print(f"{a} - {b} =",a-b)
print(f"{a} * {b} =",a*b)
print(f"{a} / {b} =",round((a/b),2))
print(f"{a} % {b} =",a%b)
print(f"{a} ^ {b} =",a**b)

#  Output:
# Enter your first number: 10
# Enter your second number: 3
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.33
# 10 % 3 = 1
# 10 ^ 3 = 1000
