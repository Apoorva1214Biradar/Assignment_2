# Ask users for marks in 5 subjects (out of 100 each). Calculate and display: 
 
# 1.	Marks in each subject   
# 2.	Total marks (out of 500)   
# 3.	Percentage   
# 4.	Grade   
# 5.	Result: Pass/Fail (Pass if all subjects >= 40) 
 

maths=int(input("Enter your maths marks:"))   #taking user inout for maths,social,science,english,kannada subjects
science=int(input("Enter your science marks:")) 
social=int(input("Enter your social marks:"))
english=int(input("Enter your english marks:"))
kannada=int(input("Enter your kannada marks:"))
total=0                                         #assinging total as 0
Total=total+int(maths+science+social+english+kannada) #calculating all subjects marks using addition
print("Total out of 500 is :",Total)
percentage=Total/500*100             #performing percentage 
print("Percentage is :",round(percentage,2))#keeping precicion upto 2 decimals
if percentage>=90:
    print("90-100 % : A+(Outstanding)")     #deciding grade for more than 90 as A+
elif percentage>80 and percentage<89:
    print("80-89 % : A(Excellent)")        #deciding grade for more than 80 and below 89 as A
elif percentage>70 and percentage<79:
    print("70-79 % : B(Good)")# and so on for 70,60 and 50 usinf elif
elif percentage>60 and percentage<69:
    print("60-69 % : C(Average)")
elif percentage>50 and percentage<59:
    print("50-59 % : D(Pass)")     
else:                         #if less than 50 then fail is displayed
    print("Below 50 % : F(Fail)")
all_subjects=maths and science and social and english and kannada
if total>=200:
    print("Result:Pass")             #if total more than 200 that means he /she has passed all subjects or secured more than 40 in all 5 subs
else:
    print("Result:Fail")   #if not fail is printed

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