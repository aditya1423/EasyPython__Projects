
menu= {
    'Pizza' : 40,
    'vada-pav': 20 ,
    'pasta': 30,
    'idli-vada': 25,
    'Tea':10,
    'Maggi':25,
    'Pav-Bhaji':50,
    'Misal-Pav': 50,
    'Puri-Bhaji': 40,
    'Coffe': 15,
    'Burger': 60
}



print("Welcome to resturant ")

print()

print("MENU CARD : ")
print(" Pizza : Rs 40\n vada-pav : Rs 20 \n pasta: Rs 30  \n idli-vada: Rs 25 \n Tea : Rs 10 \n Maggi : Rs 25 \n Pav-Bhaji : Rs 50 \n Misal-Pav : Rs 50 \n Puri-Bhaji : RS 40 \n coffe : Rs 15 \n Burger : Rs 60")



print()
order_total = 0

item1= input("Enter the name of menu : ")
print()

if item1 in menu:
    order_total=order_total+menu[item1]
    print(f"Your item {item1} has been added to your order 😁")
else:
    print(f"ordered item {item1} are not avaliable right now 🥲")
    
    
print()    

another_order= input("Do you want to add more item (YES ? NO)")

if another_order=="yes":
    item2= input("Enter the name of menu : ")
    if item2 in menu:
        order_total=order_total+menu[item2]
        print(f"Your item {item2} has been added to your order 😁") 
    else:
        print(f"ordered item {item2} are not avaliable right now 🥲")   


print(f"the total amount of bill is {order_total}")




