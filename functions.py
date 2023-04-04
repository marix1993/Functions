# Functions
# Allow you to follow DRY (don't repeat yourself)

# def - beginning of the function
# print_something - method

# def print_something():
#     print("Something has been printed.")
#
#
# print_something()

def print_something(print_string):
    print(print_string)


print_something("My name is Matty")
print_something("My second name is...")


# Java example
# public void print_string(String_text)

# def greeting(name):
#     print("Hello, my name is " + name)
#
#
# greeting("Luke")
# greeting("Fatima")


# Return statement

# def addition(int1, int2):
#     return int1 + int2
#
#
# print(addition(2, 2))

# Default arguments
# def addition(int1=2, int2=2):
#     return int1 + int2
#
#
# print(addition(10, 2))
#
#
# # Multiple arguments
#
# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
#
# multi_args(1, 2, 3, 4, 5, 6)

# Type hints
# def greeting(name: str):
#     print("Hello, my name is " + name)
#
#
# greeting(24601)

def division(denum: int, num: int) -> float:
    return denum / num


print(division(12, 5))


#
def substraction(int1: int = 5, int2: int = 2) -> int:
    return int1 - int2


print(substraction())

### Functions best practices

# 1. Name your methods using lowercase and underscores
# 2. All arguments should declare in the need and where possible their type
# 3. Remember the return statement or your function will return None
# 4. Keep your functions small as possible (break them up if possible)
# 5. Keep them readable
# 6. Use comments within your methods to help with instructions
# 7. Consider using Type Hints to avoid errors earlier
