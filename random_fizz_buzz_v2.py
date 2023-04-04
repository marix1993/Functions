# Random fizz buzz v2
import random


def get_random():
    random_number = random.randint(1, 100)
    return random_number


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return f"{number} FizzBuzz"
    elif number % 3 == 0:
        return f"{number} Fizz"
    elif number % 5 == 0:
        return f"{number} Buzz"
    else:
        return number


number = get_random()
printer = fizz_buzz(number)
print(printer)
