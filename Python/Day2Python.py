#Data types and operators
# Strings and casting
# concatenation


# x = 10
# y = 11
# print(x == y) #Checking the values as Boolean resulting True or False,
# #10 does not equal to 11
# print( x!= y) #Checking the values as Boolean resulting True or False
# #This is true as x does not equal to 11.

#Real life example:

# age = 18
# print(age < 19)


# Single quotes vs double in Python
# Using double quotes is recommended, it can gets mixed up if we use single quotes.

# print('Ugne\'s class is Eng 67 ') #Singlequotes
#
# print("Ugne's class is Eng 67") #Doublequotes
#
#Strings - indexing - casting - slicing - concatenation:
#
# greeting_welcome = "Hello World"

#Indexing starts from 0 for characters. In this case 0 would be H and 1 would be e.

# welcome_user = input("Please enter your name")
# print(" " + welcome_user + " welcome on board") #This is concatenation, if it's an integer, you have to cast it
# #into a string

# print(len(greeting_welcome)) #This will tell the length of the string in characters

#String slicing:

# hi = "Hello World"

# print(hi[0]) #The indexing starts from the beginning(left)
# print(hi[-1]) #The indexing starts from the right
# print(len(hi)) #This grabs the amount of characters
# print(hi[0:6]) #This will only print the Hello
#print(hi[6:11]) #This will print the World
#print(hi[-5:11]) #This will print the World from the right

# remove_white_space = "remove the space the end of a string          "
# print(len(remove_white_space))
#
# print(remove_white_space.strip()) #This will remove any additional space.
# print(len(remove_white_space.strip())) #This is the updated length of the string after removing the white space

# Boolean value within DATA types:

use_text = "here's SOME text with lot's of text"

print(use_text.count("text")) # This counts the substring within the string: How many times the word text is repeated in the string.

#Brings all the characters to lower case
print(use_text.lower())

#Bringing all the characters to upper case
print(use_text.upper())

#Bringing beginning of the string to upper case
print(use_text.capitalize())

#Replace tect in the string
print(use_text.replace("with", ","))

#What the string starts with, whether it's true or false
print(use_text.startswith("h"))





