# Loops - For loops are used to iterate through lists, strings, dictionaries and tuples

# list_data = [1, 2, 3, 4, 5]
# for data in list_data:
#     if data > 4:        #The iteration will only print until 4 and then it'll break
#         break
#     print(data)
#  #if and break come under each other to maintain indentation, without this, the program will not run
#
# list_data = [1, 2, 3, 4, 5]
# for data in list_data:
#     if data > 4:  #The iteration will only print until 4 and then it'll break
#         print("The data is correct")
#     elif data < 0:
#         print( "Please enter number above 0")
#     print(data)
#

# print(list_data)
# print(list_data[1])

# #create a string and loop through the string
# city = "London"
# for letter in city:
#     print(letter)

# student_record = { "name": "sohaib",
#                     "stream": "DevOps",
#                     "completed_lessons": 5,
#                     "completed_lesson_names": ["strings", "tuples", "variables"]
#
# }
#
# for record in student_record.values():
#     print(record)

# Exercise - dictionary with employee records minimum 5 key value pairs:
employee_record = {
    "name": "Sohaib",
    "employee ID": 2,
    "age": 21,
    "job role": "Dev Ops Engineer",
    "number of hours": 8.5
}
# Using loop iterate through the dictionary

for record in employee_record.keys():
    print(record)

for record in employee_record.values():
     print(record)

# display the values of values and keys of the dictionary

# While loops:
# x = 0
#
# while x < 5:
#     print(f"it's working -> {x}")
#     x += 1