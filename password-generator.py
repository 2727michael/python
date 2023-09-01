import random

# definition of a function that generates a password
def generate_password(length, all_characters):
    password = ''
    for i in range(length):
        password = ''.join([password, random.choice(all_characters)])
    return password

# definition of variables                
numbers = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
all_characters  = numbers + letters + symbols

# main program
while(True):
    try:
        length = int(input("enter a password length: "))
        if length > 0:
            break
        else:
            print("password must have some characters XD, try again")
    except ValueError:
        print("please, enter the number")

password = generate_password(length, all_characters)
print("your password:", password)
