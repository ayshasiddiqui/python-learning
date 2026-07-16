student_name = input("Enter the Student Name : ")
percentage = int(input("Enter the Percentage : "))
family_income = int(input("Enter the Family Income : "))

if percentage>=95 and family_income<350000:
    scholarship = 85000
elif percentage>=90 and family_income<300000:
    scholarship = 50000
elif percentage>=85 and family_income<250000:
    scholarship = 25000
else:
    scholarship = 0
print("Scholarship=", scholarship )