import User

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
            user_list.append(User.User(data[0], data[1], data[2], data[3], data[4], data[5]))

    current_user = None

    for user in user_list:
        if user.login(USERNAME, PASS):
            current_user = user
            break
    return current_user


def main_menu(current_user):
    menu = {}
    menu['1'] = "Edit User Information"
    menu['2'] = "Cart Information"
    menu['3'] = "Logout"
    menu['4'] = "Exit Program"
    menu['5'] = "Delete Account"
    # menu['6'] = "Add Order"  I don't really know what it means to Add order.
    menu['6'] = "Order History"

    cart = {}
    inventory = {}
    books = {}
    movies = {}
    total = {}
    accounts = {}
    history = {}

    # Add While loop over code so it will be continuous

    while True:
        print_menu(menu)
        selection = input(">> ")
        if selection == '1':  # User Information
            while True:
                menu_user = {}
                menu_user['1'] = "Change Shipping Information"
                menu_user['2'] = "Change Payment Information"
                menu_user['3'] = "Back"
                print_menu(menu_user)
                selection2 = input(">>")

                if selection2 == '1':
                    address = input("What's your shipping address")
                    print("Shipping address updated")
                elif selection2 == '2':
                    payment_info = input("Enter CC Number")
                    print("Payment information updated")
                elif selection2 == '3':
                    break
                else:
                    print("That is not an Option")
                    selection = input(menu)

        if selection == '2':  # Cart information
            menu_cart = {}
            menu_cart['1'] = "View Cart"
            menu_cart['2'] = "Add to Cart"
            menu_cart['3'] = "Checkout"
            menu_cart['4'] = "Back"

            while True:
                print_menu(menu_cart)
                selection = input(">> ")
                # remove in View

                if selection == '1':
                    print(cart)
                    menu_view = {}
                    menu_view['1'] = "View Books"
                    menu_view['2'] = "View Movies"
                    menu_view['3'] = "Remove Book"
                    menu_view['4'] = "Remove Movie"
                    menu_view['5'] = "Back"

                    while True:
                        print_menu(menu_view)
                        selection2 = input(">> ")

                        if selection2 == '1':
                            print(books)
                        elif selection2 == '2':
                            print(movies)
                        elif selection2 == '3':
                            delete_book = {}
                            delete_book = input("What book will you delete", books)
                            cart = cart - delete_book
                        elif selection2 == '4':
                            delete_movie = {}
                            delete_movie = input("What movie will you delete", movies)
                            cart = cart - delete_movie
                        elif selection2 == '5':
                            break
                        else:
                            print("Invalid selection")

                elif selection == '2':
                    menu_add = {}
                    menu_add['1'] = "Add Book"
                    menu_add['2'] = "Add Movie"
                    menu_add['3'] = "Back"
                    while True:
                        print_menu(menu_add)
                        selection2 = input(">> ")

                        if selection2 == '1':
                            book_choice = {}
                            book_choice = input("What book would you like to add?")
                            if book_choice in books:
                                cart = cart + book_choice
                            else:
                                print("Not available")

                        elif selection2 == '2':
                            movie_choice = {}
                            movie_choice = input("What movie would you like to add?")
                            if movie_choice in movies:
                                cart = cart + movie_choice
                            else:
                                print("Not available")
                        elif selection2 == '3':
                            break
                        else:
                            print("Invalid selection")

                elif selection == '3':
                    buy_now = input("Would you like to checkout Y/N")
                    if buy_now == 'Y':
                        for books in cart:
                            books = books - books in cart  # check to see if this statement will work
                        for movies in cart:
                            movies = movies - movies in cart

                        history = history + cart  # what does this do?

                    elif buy_now == 'N':
                        selection = input(menu_cart)

                elif selection == '4':
                    selection = input(menu)

                elif selection == '5':
                    break
                else:
                    print("Invalid selection")

        elif selection == '3': # logout
            logout = {}
            logout = input("Are you sure you'd like to logout, Y/N")
            if logout == 'Y':
                #current_user = None
                break

        elif selection == '4':
            exit()

        elif selection == '5':
            acct_delete = input("Would you like to delete your account, Y/N")
            if acct_delete == 'Y':
                current_user.delete_account()

        elif selection == '6':
            print(history)


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
                break
        main_menu(current_user)
    elif selection == '2':
        create_account()
    elif selection == '3':
        break
    else:
        print("Invalid selection")
