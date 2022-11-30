import pytest
from functions import *

### TODO:
'''
openFile() -- Josh
numbers() -- Josh
dist()
isPalindrome()
divide() -- 
sq() -- Zach
displayItem()--Zach
'''

########   openFile   ########
def test_openFile():
    assert openFile("testing.txt") == None

def test_openFile_int():
    assert openFile(123) == None

def test_openFile_wrong_name():
    assert openFile("test.txt") == None
##############################

########   numbers   #########
def test_numbers():
    assert numbers(8,4) == 2

def test_numbers_float():
    assert numbers(2.2, 1.1) == 2

def test_numbers_datatype():
    assert numbers('abc', [1,2,3]) == None

def test_numbers_zero():
    assert numbers(2, 0) == None
##############################

########   isPalindrome   ########
def test_isPalindrome():
    assert isPalindrome('tacocat') == True

def test_isPalindrome_false():
    assert isPalindrome('not a palindrome') == False

def test_isPalindrome_nonstring():
    assert isPalindrome([1,2,1]) == None

def test_isPalindrome_datatype():
    assert isPalindrome({'1': 'test'}) == None

def test_isPalindrome_fail():
    assert isPalindrome('abcdcba') == False


####################### divide #################
def geninputs():
	inputs = ["6", "2"]
	for item in inputs:
		yield item
GEN = geninputs()
def test_input_1(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: next(GEN))
	assert inputTest() == 3.0

def geinputus():
	inputs = ["12", "0"]
	for item in inputs:
		yield item
GEN = geninputs()
def test_input_2(monkeypatch):
	monkeypatch.setattr('builtins.input', lambda _: next(GEN))
	assert inputTest() == None

defgeninputs():
	inputs = ["Hello"]
	for item in inputs:
		yield item
GEN = geninputs()
def test_input_3(monkeypatch):
	monkeypatch.setattr('builtins.imput', lambda _: next(GEN))
	assert inputTEst() == None


################ sq ######################
def sq(num):
    return math.sqrt(num)

def test_sq():
    assert sq(4) == 2

def test_sq_2():
    assert sq(81) != 10

def test_sq_3():
    assert sq(25) == 5
    
def test_sq_4():
    assert sq(0) != int

def test_sq_5():
    assert sq(bool(4.0)) == 1.0



########   greetUser   ########
def test_greetUser(capsys):
    greetUser("Josh", "A", "Bean")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Hello!\nWelcome to the program Josh A Bean\nGlad to have you!"

def test_greetUser_datatype(capsys):
    greetUser(1, [2,3], 4.5)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Invalid input, please use strings"

def test_greetUser_numbers(capsys):
    greetUser("j0sh", "A", "22")
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Invalid input, please use letters only"

######## displayItem #########
def displayItem(numbers, index):
    numbers = "20"
    print("Your item at", index, "index is", numbers[index])


def test_displayItem(capsys):
    displayItem(20, 1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() != "Your item at 1 index is 20[1]"

def test_displayItem_2(capsys):
    displayItem(0, 1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Your item at 1 index is 0"

def test_displayItem_3(capsys):
    displayItem(3, 1)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() != "Your item at 1 index is 20[1]"
