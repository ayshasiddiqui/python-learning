customer_name = input("Enter the customer name : ")
burgers = int(input(" Enter the number of burgers : "))
pizza = int(input(" Enter the number of pizza : "))
print("Customer Name=", customer_name)
burger_rate = 80
print("Burger rate = 80")
pizza_rate = 150
print("pizza rate = 150")
total_bill = burger_rate *burgers+pizza_rate*pizza
print("Total Bill=",total_bill )
if total_bill>1000:
    discount = total_bill*10/100
else:
    discount= 0
final_amount= total_bill-discount
print("Final Amount=",final_amount )
print("Discount=",discount)
#print("Customer Name=", customer_name)
