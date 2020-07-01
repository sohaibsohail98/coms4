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
