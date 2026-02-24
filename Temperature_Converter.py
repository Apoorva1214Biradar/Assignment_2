# Create a temperature converter with a menu-based system supporting: 
# 1.	Celsius to Fahrenheit   
# 2.	Fahrenheit to Celsius   
# 3.	Celsius to Kelvin   
# 4.	Kelvin to Celsius   
# 5.	Fahrenheit to Kelvin   
# 6.	Kelvin to Fahrenheit   
# 7.	Exit 

temperature=float(input("enter an temperature you want convert:"))
print("1.Celsius to fahrenheit")
print("2.Fahrenheit to celsius")
print("3.Celsius to Kelvin")
print("4.Kelvin to Celsius")
print("5.Fahrenheit to Kelvin")
print("6.Kelvin to Fahrenheit")
print("7.Exit")
choice=int(input("enter an choice you wanted to calculate:"))
if choice==1:
    c_f=(temperature*9/5)+32
    print("C to F conversion:",c_f)
elif choice==2:
    f_c=(temperature-32)*5/9
    print("F to C conversion:",f_c)
elif choice==3:
    c_k=temperature+273.15
    print("C to K conversion:",c_k)
elif choice==4:
    k_c=temperature-273.15
    print("K to C conversion:",k_c)
elif choice==5:
    f_k=(temperature-32)*5/9+273.15
    print("F to K conversion:",f_k)
elif choice==6:
    k_f=(temperature-273.15)*9/5+32
    print("K to F conversion:",k_f)
elif choice==7:
    print("Exit")