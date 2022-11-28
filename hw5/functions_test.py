import pytest
from functions import *

### TODO:
'''
openFile() -- Josh
numbers() -- Josh
dist()
isPalindrome()
divide()
sq()
greetUser()
displayItem()
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

def test_numbers_both():
    assert numbers(2.2, 2) == 1.1