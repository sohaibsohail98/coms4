# Lists: Used in data collection

# Java and python both used arrays, the serve the same purpose of storing data

# Why list? - manage data - access data in order -  option to add, remove etc
# [] Square brackets for lists, they can be changed at any time.
# Tuple are immutable - not changeable

# Dictionary - key:value

# Let's create a list of cities

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