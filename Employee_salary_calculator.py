Employee_name = input("Enter the employee_name:")
Basic_salary = int(input("Enter the basic_salary:"))

if Basic_salary >= 50000:
  hra= Basic_salary * 20 / 100
  bonus = 5000
elif Basic_salary>= 30000:
    hra= Basic_salary * 18 / 100 
    bonus = 3000
else:
    hra= Basic_salary * 10 / 100 
    bonus = 1000

total_salary = Basic_salary + bonus + hra
print("total_salary",total_salary)
       