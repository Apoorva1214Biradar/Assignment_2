# Ask users for marks in 5 subjects (out of 100 each). Calculate and display: 
 
# 1.	Marks in each subject   
# 2.	Total marks (out of 500)   
# 3.	Percentage   
# 4.	Grade   
# 5.	Result: Pass/Fail (Pass if all subjects >= 40) 
 

maths=int(input("Enter your maths marks:"))  
science=int(input("Enter your science marks:"))
social=int(input("Enter your social marks:"))
english=int(input("Enter your english marks:"))
kannada=int(input("Enter your kannada marks:"))
total=0
Total=total+int(maths+science+social+english+kannada)
print("Total out of 500 is :",Total)
percentage=Total/500*100
print("Percentage is :",round(percentage,2))
if percentage>=90:
    print("90-100 % : A+(Outstanding)")
elif percentage>80 and percentage<89:
    print("80-89 % : A(Excellent)")
elif percentage>70 and percentage<79:
    print("70-79 % : B(Good)")
elif percentage>60 and percentage<69:
    print("60-69 % : C(Average)")
elif percentage>50 and percentage<59:
    print("50-59 % : D(Pass)")
else:
    print("Below 50 % : F(Fail)")
all_subjects=maths and science and social and english and kannada
if total>=200:
    print("Result:Pass")
else:
    print("Result:Fail")

#output 1:
# Enter your maths marks:40
# Enter your science marks:23
# Enter your social marks:43
# Enter your english marks:89
# Enter your kannada marks:69
# Total out of 500 is : 264
# Percentage is : 52.8
# 50-59 % : D(Pass)
# Result:Fail

#output 2:
# Enter your maths marks:67
# Enter your science marks:81
# Enter your social marks:89
# Enter your english marks:56
# Enter your kannada marks:42
# Total out of 500 is : 335
# Percentage is : 67.0
# 60-69 % : C(Average)
# Result:Fail