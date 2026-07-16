student_name = input("Enter the student name : ")
math_marks = int(input("Enter the math_marks : "))
science_marks = int(input("Enter the science_marks : "))
english_marks = int(input("Enter the english_marks : "))
total_marks = math_marks+science_marks+english_marks
print("total marks", total_marks)
#2total_subjects = input("enter the total_subjects:")
total_subjects = 3
max_marks = total_subjects*3
percentage=total_marks*100/max_marks
if(percentage>=95):
    print("grade A")
elif(percentage>=85):
    print("grade B")
elif(percentage>=75):
    print("grade C")
elif(percentage>=65):
    print("grade D")
else:
    print("fail")
