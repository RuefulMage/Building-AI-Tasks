import random


def main():

    rand = random.random()
    if rand < 0.1 :
        favourite = "bats"
    elif rand > 0.1 and rand < 0.2:
        favourite = "cats"
    else:
        favourite = "dogs"
    print("I love " + favourite)


main()
