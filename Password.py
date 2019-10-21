import random

def key_gen():
    keylist = random.choice('abcdefghijklmnopqrstuvwxyz')
    return keylist

def key_num():
    keynum = random.choice('0123456789')
    return keynum

def key_symbol():
    key = random.choice('!"£$%^&*@.,"')
    return key

print("This is a password generator! Please begin by inputting a random word: ", end = "")
word = input()

print("What is the name of the software, website or database this password is for?", end = "")
software = input()
software2 = software[0:2]

number = 0
list_item = ''
while number < 3:
    number = number + 1
    list_item = list_item + key_gen()
while number < 6:
    number = number + 1
    list_item = list_item + key_num()
while number < 8:
    number = number + 1
    list_item = list_item + key_symbol()

password = (word + list_item + software2)
print("Your randomly generated password is: ", end = password) 
print(". Do not share your password with anyone, except your nan, Dave down the local Co-op and that lovely smiley postman.")