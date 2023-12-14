#password generator
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$&"

while 1:
    password_len = int(input("What length of password you want : "))
    password_count = int(input("How many passwords do you want : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your Password : ", password)