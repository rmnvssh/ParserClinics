import random
import string


def number():
    second = [6, 8, 1][random.randint(0, 2)]

    third = [0, 2, 6, 8][random.randint(0, 3)]
    forth = random.randint(10, 99)
    fifth = random.randint(10, 99)

    return "(831) 2{}{}-{}-{}".format(second, third, forth, fifth)


def email_clinic(length):
    a = ["gmail.com", "outlook.com", "yandex.ru", "mail.ru"]
    type = random.choice(a)

    lettersAndDigits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(lettersAndDigits, length))

    return "{}@{}".format(rand_string, type)


def generate_password():

    password = random.randint(9999999, 100000000)
    return password
