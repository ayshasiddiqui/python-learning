customer_name = input(" Enter the customer name : ")
consumed_unit = int(input("Enter the consumed unit : "))
if consumed_unit<=100:
    rate = 5
elif consumed_unit<=300:
    rate = 7
elif consumed_unit>300:
    rate = 10
else:
    rate = 15
bill = consumed_unit* rate
print(" Electricity bill =",bill)
if consumed_unit>2000:
    discount = bill*5/100
else:
    discount= 0

final_bill = bill - discount
print("Final bill=", final_bill)
print(" Discount=", discount)