# Random guess v2
import random
import sys


def get_random_number():
    random_number = random.randint(1, 20)
    return int(random_number)


def get_user_number():
    user_number = input("Please provide your number:")
    return int(user_number)


def check_first(user_number):
    if user_number > 20:
        return "The number is too high, choose a number between 1-20."
    elif user_number == 0:
        return "You can't choose 0, choose a number between 1-20."
    elif user_number > number:
        return "Almost, bit too high. Choose one more time."
    elif user_number < number:
        return "Almost, too low. Choose one more time."
    else:
        sys.exit(print("Good guess."))


def check_second(user_number2):
    if user_number2 > 20:
        return "The number is too high, choose a number between 1-20."
    elif user_number2 == 0:
        return "You can't choose 0, choose a number between 1-20."
    elif user_number2 > number:
        return "Almost, bit too high. Choose one more time."
    elif user_number2 < number:
        return "Almost, too low. Choose one more time."
    else:
        sys.exit(print("Good guess."))


def check_third(user_number3):
    if user_number3 > 20:
        return "The number is too high, choose a number between 1-20."
    elif user_number3 == 0:
        return "You can't choose 0, choose a number between 1-20."
    elif user_number3 > number:
        return "Almost, bit too high. Choose one more time."
    elif user_number3 < number:
        return "Almost, too low. Choose one more time."
    else:
        sys.exit(print("Good guess."))


number = get_random_number()
user_number = get_user_number()
checker1 = check_first(user_number)
print(checker1)
user_number2 = get_user_number()
checker2 = check_second(user_number)
print(checker2)
user_number3 = get_user_number()
checker3 = check_third(user_number)
print(checker3)

