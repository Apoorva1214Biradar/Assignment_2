# Create a program that prints the following patterns. User should choose which pattern and height. 1	2 
# 1 2	3 
# 1 2 3	4 
# 1 2 3 4	5 

n = int(input("Height: "))   # take input from  user for pattern height (number of rows)
p = int(input("Pattern (1-4): "))  # ask user which pattern number to print

if p == 1:  # Pattern 1 selected
    for i in range(1, n+1):  # for Loop rows from 1 to n
        for j in range(1, i+1):  # Print numbers from 1 to current row number
            print(j, end=" ")  # Print number with space, stay on same line
        print()  # Move to next line after each row

elif p == 2:  # Pattern 2 selected
    for i in range(1, n+1):  # Loop rows from 1 to n
        print((str(i) + " ") * i)  # Repeat the row number i times

elif p == 3:  # Pattern 3 selected
    for i in range(n, 0, -1):  # Loop rows from n down to 1
        for j in range(i, 0, -1):  # Print numbers from i down to 1
            print(j, end=" ")  # Print number with space
        print()  # Move to next line

elif p == 4:  # Pattern 4 selected
    for i in range(1, n+1):  # Loop rows from 1 to n
        for j in range(1, i+1):  # Increasing part (1 to i)
            print(j, end="")  # Print without space
        for j in range(i-1, 0, -1):  # Decreasing part (i-1 to 1)
            print(j, end="")  # Print without space
        print()  # Moves to next line

#output 1:
# Height: 3
# Pattern (1-4): 1
# 1 
# 1 2
# 1 2 3

#output 2:
# Height: 6
# Pattern (1-4): 4
# 1
# 121
# 12321
# 1234321
# 123454321
# 12345654321