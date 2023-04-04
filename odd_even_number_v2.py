# Odd & even numbers v2

def get_number():
    number = input("Please provide number:")
    return int(number)


def check_number(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


number = get_number()
number_print = check_number(number)
print(number_print)
