#What is an API
#Application programming interface
#used to connect other programs
# in python we have a module called requests to interact with WEB-APIs

#how can we install package in pycharm
# pip install requests

import requests

# check HTTP/HTTPS 200 success - 400 - 404 page not found
response_bcc = requests.get("https://www.bbc.co.uk/")

# print(response_bcc.status_code)
# print(response_bcc.headers)
# print(response_bcc.content)
class website_check:
    def check_response_code():
        response_fb = requests.get("https://www.facebook.com/")
        if response_fb.status_code == 200:
            print("The page has been loaded successfully")
        elif response_fb.status_code == 400:
            print("Page not found")
        elif response_fb.status_code == 404:
            print("Something has gone wrong")
        else:
            pass

check_response_code()



    # print(response_bcc.status_code)
    # print(response_bcc.headers)
    # print(response_bcc.content)


# Iteration 1
# receive a response and check if 200 - print success
# elif code 400 - page not found
# else code 404 - OOPs sorry something went wrong
# 2ne Iteration
# create a function called check_response_code() including all the above
# returns the message with status code
# 3rd Iteration? OOP with 4 pillars.
