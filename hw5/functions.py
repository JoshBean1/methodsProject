import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    if type(filename) is not str:
        print("Invalid input, expected string")
        return
    try:
        infile = open(filename, "r")
    except:
        print("File opened.")
## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return
    try:
        return num1 / num2
    except:
        print("Invalid input")

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
        print("\nYour result is:", dist)
    except:
        print("\nAn error occurred")

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    try:
        test = temp[::-1]
    except:
        print("Invalid input")
        return
    if type(temp) is not str:
        print("Input string")
        return
    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        div = num1 / num2

        print("Your numbers divided is:", div)
    except ZeroDivisionError:
        print("\nYou tried to divide by zero.")
    except:
        print("\nAn error occurred")


## returns the squareroot of a particular number
def sq(num):
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    if type(first) is not str or type(middle) is not str or type(last) is not str:
        print("Invalid input, please use strings")
        return
    if not(first.isalpha()) or not(middle.isalpha()) or not(last.isalpha()):
        print("Invalid input, please use letters only")
        return

    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])
