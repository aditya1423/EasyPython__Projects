menu = {
    'Pizza': 40,
    'Vada-Pav': 20,
    'Pasta': 30,
    'Idli-Vada': 25,
    'Tea': 10,
    'Maggi': 25,
    'Pav-Bhaji': 50,
    'Misal-Pav': 50,
    'Puri-Bhaji': 40,
    'Coffee': 15,
    'Burger': 60
}

print("Welcome to the restaurant!\n")

print("MENU CARD:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")
print()

order_total = 0

while True:
    item = input("Enter the name of the menu item you'd like to order: ").title()  # Capitalize first letter
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order 😁")
    else:
        print(f"Sorry, '{item}' is not available right now 🥲")

    print()
    another_order = input("Do you want to add more items? (Yes/No): ").lower()

    if another_order != "yes":
        break

print(f"\nThe total amount of your bill is Rs {order_total}")
print("Thank you for dining with us!")




