import random

def number():
    second = [6, 8, 1][random.randint(0, 2)]

    third = [0, 2, 6, 8][random.randint(0, 3)]
    forth = random.randint(10, 99)
    fifth = random.randint(10, 99)

    return "(831) 2{}{}-{}-{}".format(second, third, forth, fifth)