# Control flow:

# Conditional statements and loops

# if, else, elif, for loop, while loop
#
# weather = "sunny"
# conditional_weather = "rainy"
#
# Conditional block of code
# if weather == "snow" and conditional_weather == "rainy":  #both conditions must be true, if any
#     #of the conditions are not met, it'll move onto the next line of code
#     print(" lets go to the beach")
# else:
#     print("Sorry better luck next time")
#
#  #Using OR operator
#  age = 18
#   if age == 18 or age > 18:  #one of the conditions must be true
#
#       print("Please proceed to check out")
#   else:
#       print("Sorry you are not eligible to watch this movie")
#
#    #Another way of doing this to simply the code:
#    age = 18
#     if age >= 18:
#         print("Please proceed to check out")
#     else:
#         print("Sorry you are not eligible to watch this movie")

# write a program to check these conditions by user input: 12, PG, 18, 15
# if age <= 17 can't watch rated 18 movie
# if age <= 12 can't watch movies above the age of 12
# display messages accordingly

age = int(input("What is your age?  "))
if  14 < age <=17:
    print("You are not allowed to watch 18 rated movies")
elif 11 < age <=14:
    print("You are not allowed to watch 15 and 18 rated movies")
elif age <= 11:
    print("You are not allowed to watch 12 and 15 and 18 rated movies")
elif age <= 0:
    print("You are allowed to watch Universal movies")
else:
    print("Welcome! Enjoy the film")



# to be 21 if would like to go to Las Vegas

age2 = int(input("What is your age?  "))

if age2 <=20:
    print("Sorry, you are not old enough to enter Las Vegas")
elif age2 >= 21:
    print("Welcome to Las Vegas! Enjoy your stay")