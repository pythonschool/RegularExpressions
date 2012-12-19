#phone number validtor

import re

pattern = "\(0(1(\d{3}\)\s\d{6}|(\d1|1\d)\)\s\d{3}\s\d{4})|2\d\)\s\d{4}\s\d{4})"

finished = False

while not finished:
    phone_number = input("Please enter your phone number: ")
    if len(phone_number) == 0:
        finished = True
    else:
        if re.match(pattern,phone_number):
            print("Valid phone number")
        else:
            print("Invalid phone number")
