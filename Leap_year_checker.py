# Create a program that checks if a year is a leap year. 

year=int(input("enter an year you want to check:")) #defined an int variable to take user input named year and converted it to integer using int() function.
if year%4==0 and year%100!=0 or year%400==0:
    print(year,":Leap year")                #Logic behind leap year: A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400.
else:
    print(year," :Not a Leap year")         #If a year is divisible by 4 and not divisible by 100, it is a leap year. However, if a year is divisible by 100, it must also be divisible by 400 to be a leap year.


#output 1:
# enter an year you want to check:2004
# 2004 :Leap year

#output 2:
# enter an year you want to check: 2026
# 2026  :Not a Leap year