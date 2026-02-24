# Create a restaurant bill splitting program. 
# Inputs: Total bill amount, Number of people, Tax percentage, Tip percentage 
# Calculate and Display: Subtotal, Tax amount, Bill after tax, Tip amount, Total bill, Amount per person 



total_bill = float(input("Enter total bill: "))        # Total bill amount
people = int(input("Number of people: "))              # Number of people
tax_percent = float(input("Tax percentage: "))         # Tax percentage
tip_percent = float(input("Tip percentage: "))         # Tip percentage


subtotal = total_bill                                  # Subtotal is original bill

tax_amount = (subtotal * tax_percent) / 100            # Calculate tax amount
bill_after_tax = subtotal + tax_amount                 # Add tax to subtotal

tip_amount = (bill_after_tax * tip_percent) / 100      # Calculate tip on bill after tax

total_amount = bill_after_tax + tip_amount             # Final total bill

amount_per_person = total_amount / people              # Split bill equally

# Display Output
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal:    ₹{subtotal:.2f}")
print(f"Tax ({tax_percent}%):   ₹{tax_amount:.2f}")
print(f"After tax:   ₹{bill_after_tax:.2f}")
print(f"Tip ({tip_percent}%):   ₹{tip_amount:.2f}")
print(f"Total:       ₹{total_amount:.2f}")
print(f"Per person:  ₹{amount_per_person:.2f}")


