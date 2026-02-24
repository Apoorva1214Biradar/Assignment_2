# Create a movie ticket pricing system. 
# Age-based Pricing:  
# Below 3: Free  
# 3-12: ₹150 (Child)  
# 13-59: ₹300 (Adult)  
# 60+: ₹200 (Senior) 
age=int(input("Enter your age:")) #defined an int variable to take user input named age and converted it to integer using int() function.
day_of_week=input("Enter the day of the week:") #defined a string variable to take user input named day_of_week to store the day of the week for which the ticket is being purchased. This will be used later to determine if a discount applies based on the day of the week.
number_of_tickets=int(input("Enter the number of tickets:")) #user input for tickets
base_price=0
if age<3: #If the age is less than 3, the ticket is free, so we print "Free" and do not calculate a base price.
    print("Free")
elif age>3 and age<12:    #If the age is between 3 and 12 (inclusive), the ticket price is ₹150, so we print "₹150(Child)" and set the base_price variable to 150 for later calculations.
    print("₹150(Child)")
    base_price=150
elif age>12 and age<60:    #if the age is between 13 and 59 (inclusive), the ticket price is ₹300, so we print "₹300(Adult)" and set the base_price variable to 300 for later calculations.
    print("₹300(Adult)")
    base_price=300
else:
    print("₹200(Senior)") #If the age is 60 or above, the ticket price is ₹200, so we print "₹200(Senior)" and set the base_price variable to 200 for later calculations.
    base_price=200
total_price=number_of_tickets*base_price
print("Base price is:",total_price) #The total price is calculated by multiplying the number of tickets by the base price per ticket, and we print the base price before applying any discounts.
if day_of_week == "saturday" or day_of_week== "sunday" or day_of_week=="friday": #If the day of the week is "saturday", "sunday", or "friday", we apply a 20% discount to the total price. We print "20% discount" and calculate the discounted total price by multiplying the total price by 0.8 (which is equivalent to giving a 20% discount). Finally, we print the total price after applying the discount.
    discount=0.2
    print("20% discount")
    total_price=total_price*0.8
    print("Total price is:",total_price)
else:                                         #If the day of the week is not "saturday", "sunday", or "friday", we do not apply any discount. We print "No discount" and the total price remains the same as the base price calculated earlier. Finally, we print the total price without any discount.
    print("No discount")
    print("Total price is:",total_price)

#output 1:ket_Pricing_System.pyesktop\Assignment_2>
# Enter your age: 10
# Enter the day of the week: wed
# Enter the number of tickets:4
# ₹150(Child)
# Base price is: 600
# No discount
# Total price is: 600

#output 2:
# Enter your age: 65
# Enter the day of the week:saturday
# Enter the number of tickets: 2
# ₹200(Senior)
# Base price is: 400
# 20% discount
# Total price is: 320.0