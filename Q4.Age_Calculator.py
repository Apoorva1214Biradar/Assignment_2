birth_year=int(input("Enter your birth year:"))
Current_age=2026-birth_year
print("Current age is:",Current_age)
Age_in_months=Current_age*12
print("Age in months is:",Age_in_months)
Age_in_days=Current_age*365
print("Age in days is:",round(Age_in_days,2))
Age_in_hours=Age_in_days*24
print("Age in hours is:",round(Age_in_hours,2))
Age_in_minutes=Age_in_hours*60
print("Age in minutes is:",round(Age_in_minutes,2))
Years_until_100=100-Current_age
print("Years until age 100:",Years_until_100)

# Output 1:
# Enter your birth year: 2004
# Current age is: 22
# Age in months is: 264
# Age in days is: 8030
# Age in hours is: 192720
# Age in minutes is: 11563200
# Years until age 100: 78

from datetime import date   # Imports the date class from datetime module to work with dates

# user inputs day , month, year in integer format
day = int(input("Enter birth day (1-31): "))     
month = int(input("Enter birth month (1-12): ")) 
year = int(input("Enter birth year: "))          

birth_date = date(year, month, day)  # Create a date object using entered year, month, and day

today = date.today()  # Get today's current date from system

age_years = today.year - birth_date.year  # Calculate rough age by subtracting birth year from current year

# Check if birthday has not happened yet this year
if (today.month, today.day) < (birth_date.month, birth_date.day):  
    age_years -= 1  # If birthday not reached yet, reduce age by 1

days_lived = (today - birth_date).days  # Calculate total number of days lived by subtracting dates

months_lived = days_lived // 30  # calculates approximate months lived by dividing days by 30
hours_lived = days_lived * 24    # Convert days lived into hours
minutes_lived = hours_lived * 60 # Convert hours lived into minutes
      
print("Years:", age_years)         
print("Months:", months_lived)     
print("Days:", days_lived)         
print("Hours:", hours_lived)       
print("Minutes:", minutes_lived)   
print("Years until 100:", 100 - age_years)

# Output 2:
# Enter birth day (1-31): 12
# Enter birth month (1-12): 04
# Enter birth year: 2003
# Years: 22
# Months: 278
# Days: 8352
# Hours: 200448
# Minutes: 12026880
# Years until 100: 78