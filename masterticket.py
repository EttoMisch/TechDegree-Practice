SERVICE_CHARGE = 2 
TICKET_PRICE = 10

tickets_remaining = 100 

def calculate(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >=0:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("What's your name?  ")
    print("Hey, {}!".format(user_name))
    number_of_tickets = input("How many ticket would you like to purchase today?  ")
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print ("Please, try again! {}".format(err))
    else:
        total_price = calculate(number_of_tickets)
        print("Your total for {} tickets will be {}$, including of a {}$ service charge.".format(number_of_tickets,total_price,SERVICE_CHARGE))
        purchase = input("{}, would you like to go ahead with your purchase?  yes/no  ".format(user_name))
        if purchase.lower() == "y":
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("No worries {}, hope to see you soon!".format(user_name))
        
print ("Sorry, {}, there are no more tickets available for this show".format(user_name))
