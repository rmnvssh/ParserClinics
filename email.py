import random
import string

def emailClinic(length):
    a = ["gmail.com", "outlook.com", "yandex.ru", "mail.ru"]
    type = random.choice(a)

    lettersAndDigits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(lettersAndDigits,length))

    return "{}@{}".format(rand_string, type)
