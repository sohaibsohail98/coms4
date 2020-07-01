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

# use_text = "here's SOME text with lot's of text"
#
# print(use_text.count("text")) # This counts the substring within the string: How many times the word text is repeated in the string.
#
# #Brings all the characters to lower case
# print(use_text.lower())
#
# #Bringing all the characters to upper case
# print(use_text.upper())
#
# #Bringing beginning of the string to upper case
# print(use_text.capitalize())
#
# #Replace tect in the string
# print(use_text.replace("with", ","))
#
# #What the string starts with, whether it's true or false
# print(use_text.startswith("h"))

#Lists: Used in data collection

#Java and python both used arrays, the serve the same purpose of storing data

#Why list? - manage data - access data in order -  option to add, remove etc
#[] Square brackets for lists, they can be changed at any time.
#Tuple are immutable - not changeable

#Dictionary - key:value

#Let's create a list of cities

# cities = ["Tokyo", "Paris", "Prague", "Luxembourg"]
# #display (print()) list the cities
# print(cities)
# print(type(cities)) #This will tell the type of data, in this case class list.
#
# print(cities[3]) #This will print Luxembourg within the list.
# cities[3] = "Amsterdam" #This will replace a string within the list.
#
# print(cities)
#
# cities.append("Vilnius") #This will add the value to the list at the end
# # print(cities)
#
# cities.remove("Paris") #This will remove the value from the list
# print(cities)
#
# cities.pop()  #Deletes the last index in the list
# print(cities)
#
# cities.insert(0, "London") #Add the value in the particular index, in this case in the beginning
# print(cities)
#
# #Lists can hold multiple data types
# mix_type_string = [1, 2, 3]
# string_list = ["one", "two", "three"]
# print(mix_type_string + string_list) #This will combine the two lists.

#Tuples - storing data that isn't needed to be changed - eg: DOB, NHS ID

#Syntax of Tuple: we use () to create a Tuple

user_details = ("name", "dob", "passport number")
print(user_details)

print(user_details[1])

#Convert the tuple into an list
#add your name into the string at 0 index
#display the list

user_details_list =list(user_details) #Convert the tuple into an list
print(user_details_list)

print(type(user_details_list))

user_details_list.insert(0,"James")   #add your name into the string at 0 index
print(user_details_list) #display the list





