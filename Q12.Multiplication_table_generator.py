#Create a program that asks the user for a number and a range, then displays the multiplication table. 

number = int(input("Enter number: "))        # Stores the number for multiplication
end_range = int(input("Enter range (end): "))  # Stores how far the table should go

print("\nMultiplication Table of", number)   # Displays heading

# Loop to generate table
for i in range(1, end_range + 1):            # Loop from 1 to given range
    print(number, "x", i, "=", number * i)  

# Full Multiplication Table (1–10)

print("\nFull Multiplication Table (1-10)\n")

for i in range(1, 11):              # Rows (1 to 10)
    for j in range(1, 11):          # Columns (1 to 10)
        print(i * j, end="\t")      # \t gives tab space 
    print()                         # Move to next row

#output 1:
# Enter number:  3
# Enter range (end):  4

# Multiplication Table of 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12

# Full Multiplication Table (1-10)

# 1       2       3       4       5       6       7       8       9       10
# 2       4       6       8       10      12      14      16      18      20
# 3       6       9       12      15      18      21      24      27      30
# 4       8       12      16      20      24      28      32      36      40
# 5       10      15      20      25      30      35      40      45      50
# 6       12      18      24      30      36      42      48      54      60
# 7       14      21      28      35      42      49      56      63      70
# 8       16      24      32      40      48      56      64      72      80
# 9       18      27      36      45      54      63      72      81      90
# 10      20      30      40      50      60      70      80      90      100


#output 2:
# Enter number:  7
# Enter range (end):  5
# Multiplication Table of 7
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35

# Full Multiplication Table (1-10)

# 1       2       3       4       5       6       7       8       9       10
# 2       4       6       8       10      12      14      16      18      20
# 3       6       9       12      15      18      21      24      27      30
# 4       8       12      16      20      24      28      32      36      40
# 5       10      15      20      25      30      35      40      45      50
# 6       12      18      24      30      36      42      48      54      60
# 7       14      21      28      35      42      49      56      63      70
# 8       16      24      32      40      48      56      64      72      80
# 9       18      27      36      45      54      63      72      81      90
# 10      20      30      40      50      60      70      80      90      100





