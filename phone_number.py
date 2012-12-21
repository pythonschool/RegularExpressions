#phone number validtor

import re

pattern = """\(0                   #open bracket followed by a zero
                                     #then either:
               (
                   1                 #1
                                     #followed by either:
                   (
                       \d{3}         #3 digits
                       \)            #close bracket
                       \s            #single space
                       \d{6}         #6 digits
                   |                 #or
                       (
                           \d1       #a single digit followed by a 1
                       |             #or
                           1\d       #a 1 followed by a single digit
                       )
                       \)            #a close bracket
                       \s            #a single space
                       \d{3}         #3 digits
                       \s            #a single space
                       \d{4}         #4 digits
                   )
               |                     #or
                   2\d\)             #2 followed by a digit and a close bracket
                   \s                #a single space
                   \d{4}             #4 digits
                   \s                #a single space
                   \d{4}             #4 digits
               )$"""

finished = False

while not finished:
    phone_number = input("Please enter your phone number: ")
    if len(phone_number) == 0:
        finished = True
    else:
        if re.match(pattern,phone_number,re.VERBOSE):
            print("Valid phone number")
        else:
            print("Invalid phone number")
