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
accounts  = {}
history = {}

#Add While loop over code so it will be continuous

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

        if selection2 == '1':
            print(books)
        if selection2 == '2':
            print(movies)
        if selection2 == '3':
            delete_book = {}
            delete_book = input("What book will you delete", books)
            cart = cart - delete_book
        if selection2 == '4':
            delete_movie = {}
            delete_movie = input("What movie will you delete", movies)
            cart = cart - delete_movie

    if selection == '2':
        menu_add = {}
        menu_add['1'] = "Add Book"
        menu_add['2']  = "Add Movie"
        selection2 = input(menu_add)

        if selection2 == '1':
            book_choice = {}
            book_choice = input("What book would you like to add?")
            if book_choice in books:
                cart = cart + book_choice
            else:
                print ("Not available")

        if selection2 == '2':
            movie_choice = {}
            movie_choice = input("What movie would you like to add?")
            if movie_choice in movies:
                cart = cart + movie_choice
            else:
                print ("Not available")

        else:
            print("not an option")
            selection = input(menu_add)

    if selection == '3':
        buy_now = {}
        buy_now = input("Would you like to checkout Y/N")
        if buy_now == 'Y':
            for books in cart:
                books = books - books in cart         #check to see if this statement will work
            for movies in cart:
                movies = movies - movies in cart
        
        history = history + cart

        if buy_now == 'N':
            selection = input(menu_cart)

    



    if selection == '4':
        selection = input(menu)

if selection == '3':
    logout = {}
    logout = input("Are you sure you'd like to logout, Y/N")
    if logout == 'Y':
        lougout = True
    if logout == 'N':
        selection = input(menu)
    #initiate logout function

if selection == '4':
    exit()

if selection == '5':
    acct_delete = {}
    acct_delete = input("Would you like to delete your account, Y/N")
    if acct_delete == 'Y':
        acct = {}
        acct = input("Name on account")
        if acct in accounts:
            accounts = accounts - acct

if selection == '6':
    print(history)
    selection = input(menu)