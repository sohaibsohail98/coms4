#
# #Creating a variable
#
# x = 10 #Type of integer
#
# print("hello world")
#
# y = 3.6 #float
# name = "Sparta" #String
#
# print(x)
#
# print(y)
# print(x + y)
#
# print(type(name))
#
# print(x + name) #You can't run a integer with a string.
# print(str(x) + name) #This is a way to fix that. Casting the integer value as a string.


# age = input("Please enter your age") #This is to store the value what the user inputs.
# print(age) #This will print the user input
#
# name = input("Please enter your name") #Thid will store the name of what the user inputs.
# print(name) #This will print the user input

#Overwriting the variable:

# name = "sohaib"
# print(name)
# name = "bond" #The value of name has changed, it has been overwriting.
# print(name)

#Exercise, capturing user details:

#Create a variable called first_name and last_name,
first_name = "Sohaib"
last_name = "Sohail"

#Create a variable called full_name and display full_name

full_name = first_name + " " + last_name
# print(full_name)

#Create a variable called age
age = 21

#Create a variable called address
address = "23 Downing Street"

#Enter the user's details:

print(full_name + " " + str(age) + " " + address)

