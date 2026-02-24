# Create an ATM simulation with initial balance = ₹10,000. 
# Menu: 1. Check Balance  2. Deposit Money  3. Withdraw Money  4. Exit 

balance=10000 #defined a variable named balance and assigned it an initial value of 10000, representing the starting balance in the ATM simulation. This variable will be used to keep track of the user's current balance as they perform various transactions such as checking their balance, depositing money, or withdrawing money.
print("1. Check Balance") #The program then prints a menu with four options for the user to choose from: "1. Check Balance", "2. Deposit Money", "3. Withdraw Money", and "4. Exit". This menu provides the user with different actions they can take within the ATM simulation.
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choice=int(input("Enter your choice:")) # choices for user to select an option from the menu. 
if choice==1:
        print("Your balance is:",balance) #if the user selects option 1, the program will print the current balance by accessing the value stored in the balance variable. This allows the user to check how much money they have in their account before deciding on any further actions.
elif choice==2:
        deposit_amount=float(input("Enter the amount you want to deposit:")) #If the user selects option 2, the program prompts them to enter the amount they want to deposit. The input is taken as a string and then converted to a floating-point number using the float() function, allowing for decimal values in case the user wants to deposit an amount that includes cents.
        balance=balance+deposit_amount
        print("Your new balance is:",balance)
elif choice==3:
        withdraw_amount=float(input("Enter the amount you want to withdraw:")) #If the user selects option 3, the program prompts them to enter the amount they want to withdraw. Similar to the deposit option, the input is taken as a string and converted to a floating-point number using the float() function. This allows for decimal values in case the user wants to withdraw an amount that includes cents.
        if withdraw_amount>balance:    #Before processing the withdrawal, the program checks if the requested withdrawal amount exceeds the current balance. If the withdraw_amount is greater than the balance, it means the user does not have enough funds to complete the transaction, and the program will print "Insufficient balance" to inform the user that they cannot withdraw that amount.
            print("Insufficient balance")
        else:
            balance=balance-withdraw_amount #If the withdrawal amount is less than or equal to the current balance, the program proceeds with the withdrawal by subtracting the withdraw_amount from the balance variable. This updates the user's balance to reflect the amount they have withdrawn.
            print("Your new balance is:",balance)
elif choice==4:
    print("Thank you for using the ATM. Goodbye!") #If the user selects option 4, the program will print a farewell message thanking the user for using the ATM and saying goodbye. This indicates that the user has chosen to exit the ATM simulation, and the program will end after displaying this message.

else:
    print("Invalid choice. Please try again.") 

# output 1:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# Enter your choice:1
# Your balance is: 10000


# output 2:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# Enter your choice:3
# Enter the amount you want to withdraw: 3000
# Your new balance is: 7000.0