# # try:
# #     result=10/0
# #
# # except catch ZeroDivisionError:
# #     print("Opss! Tried to divide by zero!")
# from conditionals import number
#
# fruits = {
#     "apple":5,
#     "Orange":3,
#     "banana":7,
# }
#
# try:
#     print(fruits["cherry"])
#
# except KeyError:
#     print("The key does not mach in the dictionary")
#
#
# text = "This is not a number"
#
# try:
#     text_to_int = int(text)
#
# except Exception as e:
#     print("An error occurred", e)
#
# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("Division by 0")
# else:
#     print("Division successful.Result=", result)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("We have an error, we cant divide by 0")
# finally:
#     print("Finally block executed")
#
# def divide_numbers(a,b):
#     try:
#         result = a/b
#         print("The result is: ", result)
#     except ZeroDivisionError:
#         print("You tried to divide by 0")
#     except TypeError:
#         print("Invalid type for division")
#     except Exception as e:
#         print("Unexpected error", e)
#     else:
#         print("Unexpected Error")
#
# divide_numbers(10,2)
# divide_numbers(10,0)
# divide_numbers(10,'2')
#

def number(number1, number2, operator):
    if operator=="+":
        return number1+number2
    elif operator=="-":
        return number1-number2
    elif operator=="*":
        return number1*number2
    elif operator=="/":
        return number1/number2
    else:
        raise ValueError("Invalid operator")

try:
    number1=float(input("Type number1 "))
    operator=(input("Enter an operator(+,-,*,/) "))
    number2 = float(input("Type number2 "))
    result =number (number1, number2, operator)
    print("Result:", result)
except ZeroDivisionError:
    print("You tried to divide by 0")
except TypeError:
    print("Invalid type for division")
except Exception as e:
    print("Unexpected error", e)
else:
    print("You did it")



