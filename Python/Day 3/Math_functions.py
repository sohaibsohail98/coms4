#How can we use builtin python library

# from random import random #From is another way of "def" to call a function.
# import math     #import built in modules

# To generate a random number - mostly in lotteries.
# print(random())

# float_num = 24.5  #float

# round the float number

# print(math.ceil(float_num)) #This will round the value up
# print(math.floor(float_num)) #This will round the value down

#One of these need to be executed depending on the decimal value
# print(math.pi)

#Create a method that would take two arguments

# def multiple_arguments(*manyargs):
#     print(manyargs())
#
#     for args in manyargs:
#         return args

# user would like to convert 7 inches into cm

# def cm_to_inch(float_1, float_2):
#
# float_3 = float_1 + float_2
# return (float_3/2.54)
import math

def cm_to_inches(cm):
    print("the value of cm into inches is")
    return(math.ceil(cm/2.54))
print(cm_to_inches(10))


#Calculate cm into inches or vise versa