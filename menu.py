from User import User
from Inventory import Inventory
from movieandbook import *
from cart import Cart


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
            user_list.append(User(data[0], data[1], data[2], data[3], data[4], data[5], data[6].replace('\n','')))

    current_user = None

    for user in user_list:
        if user.login(USERNAME, PASS):
            current_user = user
            break
    return current_user


def main_menu(current_user):
    book_list = list()
    movie_list = list()

    user_cart = Cart(current_user.ID)

    with open('books.txt', 'r') as book_file:
        lines = book_file.readlines()
        for line in lines:
            data = line.split(',')
            book_list.append(Book(data[0], data[1], data[2], data[3]))

    with open('movies.txt', 'r') as movie_file:
        lines = movie_file.readlines()
        for line in lines:
            data = line.split(',')
            movie_list.append(Movie(data[0], data[1], data[2], data[3]))

    inventory = Inventory(book_list, movie_list)
    order_history = list()


    menu = {}
    menu['1'] = "Edit User Information"
    menu['2'] = "View/Edit Cart"
    menu['3'] = "Shop"
    menu['4'] = "Checkout"
    menu['5'] = "Order History"
    menu['6'] = "Logout"
    menu['7'] = "Exit Program"
    menu['8'] = "Delete Account"



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
                    user_cart.view_cart()


                elif selection == '2':  # view books
                    user_cart.view_books()


                elif selection == '3':  # view movies
                    user_cart.view_movies()

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
                            user_cart.view_books()
                            delete_book = input("What book will you delete? (Enter the ID of the book): ")
                            user_cart.remove_book_ID(delete_book)  # replace with correct cart function
                        elif selection2 == '2':
                            user_cart.view_movies()
                            delete_movie = input("What movie will you delete? (Enter the ID of the movie): ")
                            user_cart.remove_movie_ID(delete_movie)  # see above
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
                    inventory.view_books()
                    print("Which book do you want to add to your cart? Or type 'cancel' to go back.")
                    toBuy = input(">> ")
                    if toBuy != "cancel":
                        addBook = inventory.get_book_ID(toBuy)
                        user_cart.add_book(addBook)

                elif selection == '2':  # movies
                    inventory.view_movies()
                    print("Which movie do you want to add to your cart? Or type 'cancel' to go back.")
                    toBuy = input(">> ")
                    if toBuy != "cancel":
                        addMovie = inventory.get_movie_ID(toBuy)
                        user_cart.add_movie(addMovie)
                elif selection == '3':
                    break
                else:
                    print("Invalid selection")

        elif selection == '4':  # checkout
            order_list = list()
            for key in user_cart.books:
                i = 0
                while i < key.count:
                    order_list.append(inventory.get_book_ID(key.ID))
                    print("Checked out ", key.name, " from inventory.\n")
                    inventory.checkoutBook(key.ID)
                    i = i + 1

            for key in user_cart.movies:
                i = 0
                while i < key.count:
                    order_list.append(inventory.get_movie_ID(key.ID))
                    print("Checked out ", key.name, " from inventory.\n")
                    inventory.checkoutMovie(key.ID)
                    i = i + 1
            order_history.append(order_list)

            user_cart.remove_all_items()


        elif selection == '5':  # view order history
            index = 1
            for order in order_history:
                print("Order", index)
                for item in order:
                    print(item.name, '$' +  item.price)
                index += 1

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
