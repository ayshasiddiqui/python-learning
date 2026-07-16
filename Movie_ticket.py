customer_name = input("Enter the Customer Name : ")
customer_age = int(input("Enter the Customer Age : "))
tickets = int(input("Enter the number of Tickets : "))
if customer_age< 5 :
    ticket_price = 0    
elif customer_age < 12 :
    ticket_price = 100
    #print("Ticket Price=", ticket_price )
elif customer_age <60:
    ticket_price = 200
   # print("Ticket Price=", ticket_price )
else:
    ticket_price = 150
    #print("Ticket Price=", ticket_price )
final_amount  = ticket_price * tickets
print("Final amount=",final_amount ) 
print("Ticket Price=", ticket_price )