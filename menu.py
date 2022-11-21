menu = {}
menu['1'] = "Edit User Information"
menu['2'] = "Cart Information"
menu['3'] = "Logout"
menu['4'] = "Exit Program"
menu['5'] = "Delete Account"
menu['6'] = "Add Order"
menu['7'] = "Order History"

cart = {}
inventory = {}

selection = input(menu)
if selection == '1':
    menu_user = {}
    menu_user['1'] = "Change Shipping Information"
    menu_user['2'] = "Change Payment Information"
    selection2 = input(menu_user)


    if selection2 == '1':
        address = input("What's your shipping address")
        print("Shipping address updated")
    if selection2 == '2':
        payment_info = input("Enter CC Number")
        print("Payment information updated")
     
    else:
            print("That is not an Option")
            selection = input(menu)


if selection == '2':
    menu_cart = {}
    menu_cart['1'] = "View Cart"
    menu_cart['2'] = "Add to Cart"
    menu_cart['3'] = "Checkout"
    menu_cart['4'] = "Go Back"
    selection = input(menu_cart)
#remove in View

    if selection == '1':
        print(cart)

        menu_view = {}
        menu_view['1'] = "View Books"
        menu_view['2'] = "View Movies"
        menu_view['3'] = "Remove Book"
        menu_view['4'] = "Remove Movie"
        selection2 = input(menu_view)



