import random
import string
import sys

def gen_password(length: int): 
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    special = list("~!@#$%&*()-_=+][{}\";:'/?.>,<|")

    password_chars = [
        lowercase.pop(random.randint(0, len(lowercase) - 1)),
        uppercase.pop(random.randint(0, len(uppercase) - 1)),
        digits.pop(random.randint(0, len(digits) - 1)),
        special.pop(random.randint(0, len(special) - 1)),
    ]

    all_chars = lowercase + uppercase + digits + special

    password_chars += random.sample(all_chars, length - 4)

    random.shuffle(password_chars)

    return ''.join(password_chars)

def gen_long_password(length: int):
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    special = list("~!@#$%&*()-_=+][{}\";:'/?.>,<|")

    password_chars = [
        lowercase[random.randint(0, len(lowercase) - 1)],
        uppercase[random.randint(0, len(uppercase) - 1)],
        digits[random.randint(0, len(digits) - 1)],
        special[random.randint(0, len(special) - 1)],
    ]

    all_chars = lowercase + uppercase + digits + special

    password_chars += random.choices(all_chars, k=length - 4)

    random.shuffle(password_chars)

    return ''.join(password_chars)

if len(sys.argv) < 2:
    print(gen_password(16))
else:
    if sys.argv[1].isdigit():
        if int(sys.argv[1]) < 4:
            print('Length must be a number greater than 4')
        elif int(sys.argv[1]) > 91:
            print(gen_long_password(int(sys.argv[1])))
        else:
            print(gen_password(int(sys.argv[1])))
    else:
        print('Length must be a number greater than 4')