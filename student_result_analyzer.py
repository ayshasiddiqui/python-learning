Student_name = input("enter the student name : ")
#subject_marks = int(input("enter the 5 subject marks: "))
english_marks = int(input("enter the english marks :"))
math_marks = int(input("enter the math marks :"))
handi_marks = int(input("enter the hindi marks:"))
science_marks = int(input("rnter the science marks :"))
drawing_marks = int(input("enter the drawing marks :"))
total_marks = english_marks + math_marks + handi_marks + science_marks + drawing_marks
print("total marks=", total_marks)
percentage = total_marks*100/500
print("percentage=", percentage)

if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("grade B")
elif percentage>=70:
    print("grade C")
elif percentage>=60:
    print("grade D")
else:
    print("fail")

