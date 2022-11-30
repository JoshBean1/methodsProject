from User import User
from Inventory import Inventory
from movieandbook import *
from cart import Cart


book_list = list()
movie_list = list()



def print_menu(menu):
    for key in menu:
        print(key + '. ' + menu[key])

def login(USERNAME, PASS):  # if success, returns user class
    user_list = []
    with open('users.csv', 'r') as user_file:
        lines = user_file.readlines()
        #print(lines)
        for line in lines:

            data = line.split(',')
            user_list.append(User(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

    current_user = None

    for user in user_list:
        if user.login(USERNAME, PASS):
            current_user = user
            break
    return current_user


def main_menu(current_user):
    menu = {}
    menu['1'] = "Edit User Information"
    menu['2'] = "View/Edit Cart"
    menu['3'] = "Shop"
    menu['4'] = "Checkout"
    menu['5'] = "Order History"
    menu['6'] = "Logout"
    menu['7'] = "Exit Program"
    menu['8'] = "Delete Account"


    cart = {}


    while True:
        print_menu(menu)
        selection = input(">> ")
        if selection == '1':  # User Information
            while True:
                menu_user = {}
                menu_user['1'] = "Change Shipping Information"
                menu_user['2'] = "Change Payment Information"
                menu_user['3'] = "Change name"
                menu_user['4'] = "Change password"
                menu_user['5'] = "Back"
                print_menu(menu_user)
                selection2 = input(">>")

                if selection2 == '1':
                    address = input("What's your shipping address: ")
                    current_user.change_address(address)
                    print("Shipping address updated")
                elif selection2 == '2':
                    payment_info = input("Enter CC Number: ")
                    current_user.change_payment_info(payment_info)
                    print("Payment information updated")
                elif selection2 == '3':
                    name = input("Enter new name: ")
                    current_user.change_name(name)
                    print("Name updated")
                elif selection2 == '4':
                    while True:
                        current_pass = input("Input current password or type 'cancel' to cancel: ")
                        if current_pass == 'cancel':
                            break
                        elif current_pass == current_user.password:
                            new_pass = input("Enter new password: ")
                            current_user.change_pass(new_pass)
                            break
                        else:
                            print("Incorrect password")
                elif selection2 == '5':
                    break
                else:
                    print("That is not an Option")
                    selection = input(menu)

        elif selection == '2':  # view/edit cart; TODO- implement cart class
            menu_cart = {}
            menu_cart['1'] = "View All"
            menu_cart['2'] = "View Books"
            menu_cart['3'] = "View Movies"
            menu_cart['4'] = "Edit Cart"
            menu_cart['5'] = "Back"

            while True:
                print_menu(menu_cart)
                selection = input(">> ")

                if selection == '1':  # view all
                    print(cart)  # cart.view_all()


                elif selection == '2':  # view books
                    pass  # cart.view_books()?


                elif selection == '3':  # view movies
                    pass  #

                elif selection == '4':  # edit cart
                    #  cart.view_all()

                    menu_edit = {}
                    menu_edit['1'] = "Remove Book"
                    menu_edit['2'] = "Remove Movie"
                    menu_edit['3'] = "Back"

                    while True:  # TODO: cart class needs to be correctly implemented here
                        print_menu(menu_edit)
                        selection2 = input(">> ")


                        if selection2 == '1':
                            delete_book = input("What book will you delete? ")
                            cart = cart - delete_book  # replace with correct cart function
                        elif selection2 == '2':
                            delete_movie = input("What movie will you delete? ")
                            cart = cart - delete_movie  # see above
                        elif selection2 == '3':
                            break
                        else:
                            print("Invalid selection")
                elif selection == '5':
                    break

                else:
                    print("Invalid selection")

        elif selection == '3':
            menu_shop = {}
            menu_shop['1'] = "Shop for Books"
            menu_shop['2'] = "Shop for Movies"
            menu_shop['3'] = "Back"
            while True:
                print_menu(menu_shop)
                selection = input(">> ")

                if selection == '1':  # books
                    #inventory.view_books()
                    print("Which book do you want to add to your cart? Or type 'cancel' to go back.")
                    toBuy = input(">> ")
                    if toBuy != "cancel":
                        pass  # cart.add_book or book.add_to_cart or something

                elif selection == '2':  # movies
                    #inventory.view_movies()
                    print("Which movie do you want to add to your cart? Or type 'cancel' to go back.")
                    toBuy = input(">> ")
                    if toBuy != "cancel":
                        pass  # cart.add_movie
                elif selection == '3':
                    break
                else:
                    print("Invalid selection")

        elif selection == '4':  # checkout
            #cart.checkout()
            #  add order to order_history.csv
            pass

        elif selection == '5':  # view order history
            with open("order_history.csv", 'r') as history:
                for lines in history.readlines():
                    print(line)  # make this more pretty

        elif selection == '6': # logout
            logout = input("Are you sure you'd like to logout? Y/N: ")
            if logout.lower() == 'y' or logout.lower() == 'yes':
                #current_user = None
                break

        elif selection == '7':
            exit()

        elif selection == '8':
            acct_delete = input("Would you like to delete your account? Y/N: ")
            if acct_delete == 'Y':
                current_user.delete_account()
                break


while True:
    start_menu = {}
    start_menu['1'] = "Login"
    start_menu['2'] = "Create Account"
    start_menu['3'] = "Exit"
    print_menu(start_menu)
    selection = input(">> ")

    if selection == '1':
        while True:
            USERNAME = input("Username: ")
            PASS = input("Password: ")
            current_user = login(USERNAME, PASS)
            if current_user is None:
                print("Invalid username or password")
            else:
                print("Successful login\n")
                break
        main_menu(current_user)
    elif selection == '2':
        name = input("Input Name: ")
        username = input("Input Username: ")
        email = input("Input email: ")
        payment_info = input("Input payment info: ")
        address = input("Input shipping address: ")
        password = input("Input password: ")

        user_list = []
        with open('users.csv', 'r') as user_file:
            lines = user_file.readlines()
            for line in lines:
                data = line.split(',')
                user_list.append(int(data[0]))
        new_ID = str(max(user_list) + 1)
        new_user = User(new_ID, username, password, name, payment_info, address, email, new=True)
        print("User created")
    elif selection == '3':
        break
    else:
        print("Invalid selection")
