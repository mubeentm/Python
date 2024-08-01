import csv




def menu():
    print("Select one option from menu")

    print("1.View the item\n2.Add to cart\n3.Update the cart\n4.Remove from cart\n5.Exit and print")


def show(availabe_item):
    print("ITEM\t\tPRICE")

    for i in availabe_item:
        print(i, "\t\t", availabe_item[i])


def view_cart(availabe_item, main_stock):
    for i in availabe_item:
        print(i, availabe_item[i], 'Qty', "Rs", availabe_item[i] * main_stock[i])


def add_item_to_cart():
    item_name = input("Enter the name of item to add : ")

    if (item_name not in availabe_item.keys()):

        print("\n---ITEM NOT FOUND!!!---\n")

    elif (item_name in cart.keys()):

        print("\n---ITEM ALREADY EXIST!!!---\n")

    else:

        cart[item_name] = int(input("Enter the Quantity"))


def update_item():
    item_name = input("Enter the name of item to add : ")

    if (item_name not in availabe_item.keys()):

        print("\n---ITEM NOT FOUND!!!---\n")

    elif (item_name in cart.keys()):

        cart[item_name] = int(input("Enter the Quantity"))

    else:

        print("\n---ITEM NOT FOUND!!!---\n")


def delete_item_from_cart():
    item_name = input("Enter the item to be removed : ")

    if (item_name not in stock.keys()):

        print("\n---ITEM NOT FOUND!!!---\n")

    else:

        cart.pop(item_name)


def print_bill():
    total = 0

    item_index = 1

    print("*" * 10, " TOTAL BILL ", "*" * 10)

    print("Si.No.\tITEM\tQUANTITY\tPRICE")

    for i in cart:
        print(item_index, ".\t", i, '\t', cart[i], "\t\tRs.", cart[i] * availabe_item[i])

        item_index += 1

        total += cart[i] * availabe_item[i]

    print("Total price Rs.", total)


# *********************************************


print("*" * 19)

print("Welcome to my store")

print("*" * 19)

availabe_item = {"BREAD": 40, "CHEESE": 90, "MILK": 30, "CHOCLATE": 100, "FLOUR": 40, "BOOK": 40}

cart = {}

menu()

user_input = int(input())

if user_input not in [1, 2, 3, 4, 5]:
    print("Enter correct value!")

while (user_input != 5):

    if user_input == 1:

        show(availabe_item)

        menu()

        user_input = int(input())


    elif (user_input == 2):

        add_item_to_cart()

        view_cart(cart, availabe_item)

        menu()

        user_input = int(input())

    elif (user_input == 3):

        update_item()

        view_cart(cart, availabe_item)

        menu()

        user_input = int(input())

    elif (c == 4):

        delete_item_from_cart()

        view_cart(cart, availabe_item)

        menu()

        user_input = int(input())

if (user_input == 5):
    print_bill()
