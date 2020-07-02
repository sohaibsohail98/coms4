#What is a function?

#Why should we use function, what is the benefit - referring and reusing code
# What functions have we used so far?
# DRY - Don't repeat yourself


#Syntax: - def - name of the function with () and :

# def greeting():
#     return "welcome to the program"

# pass - used to skip the function
# in order to print the function, you need to call it.

# print(greeting())

#This will display the string from the function, by calling it.

# def test():
#     pass
#This will skip the process of the function - its methods, returning no outcome
# It is used in creating or building a unit test

#methods with parameters/arguments:

# def add_values()
#     return 4 + 4 #We can return anything - string or integer - this was with a + operator,
#
# print(add_values())

#Storing and returning values from the function method
# def addition_values(number1, number2):
#     return number1 + number2
#
# print(addition_values(4, 9))
#
# #create a function with two arguments to return a subtration of the 2 values given
#
# def subtration_values(number1, number2):
#     return number1 - number2
#
# print(subtration_values(10,5))
#
# #create a function with two arguments to return a division of the 2 values given
#
# def division_values(number3, number4):
#     return number3 - number4
#
# print(division_values(55,5))
#
# #create a function with two arguments to return a remainder of the 2 values given
#
# def remainder_values(number5, number6):
#     return number5 % number6
#
# print(remainder_values(61, 3))
#
# #create a function with two arguments to return * of the 2 values given
#
# def multiplication_values(number7, number8):
#     return number7 * number8
#
# print (multiplication_values(90, 2))
#
# user_input = int(input(multiplication_values()))

#Create a function with multiple arguments

# def multi_args(*multiargs):
#     print(type(multiargs()))
#
#     for args in multiargs:
#         print(args)
#     return args
# print(multi_args(1, 2, 3, 4, 5, 6))



