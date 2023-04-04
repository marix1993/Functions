# Basic calculator

# def addition(int1: int, int2: int) -> int:
#     return int1 + int2
#
#
# print("Addition: Please provide first number")
# int1 = int(input())
# print("Please provide second number")
# int2 = int(input())
# print(addition(int1, int2))
#
#
# def subtraction(int1: int, int2: int) -> int:
#     return int1 - int2
#
#
# print("Subtraction: Please provide first number")
# int1 = int(input())
# print("Please provide second number")
# int2 = int(input())
# print(subtraction(int1, int2))
#
#
# def multiplication(int1: int, int2: int) -> int:
#     return int1 * int2
#
#
# print("Multiplication: Please provide first number")
# int1 = int(input())
# print("Please provide second number")
# int2 = int(input())
# print(multiplication(int1, int2))
#
#
# def division(int1: int, int2: int) -> float:
#     return int1 / int2
#
#
# print("Division: Please provide first number")
# int1 = int(input())
# print("Please provide second number")
# int2 = int(input())
# print(division(int1, int2))


def cm_converter(num) -> int:
    return num * 0.01


print("Please provide value in cm")
num = int(input())
print(f"Converting {num}cm into {cm_converter(num)} meters.")


def feet_converter(num1) -> int:
    return num1 * 3.28084


print("Please provide value in m")
num1 = int(input())
print(f"Converting {num1}m into {feet_converter(num1)} feet.")

