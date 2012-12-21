#car registration validtor

import re

pattern = """
               [A-Z]            #single letter
                                #followed by either:
               (
                   (
                       [A-Z]    #single letter
                       \d{2}    #2 digits
                   |            #or
                       \d{1,3}  #between 1 and 3 digits
                   )
                                #followed by:
                   [A-Z]{3}     #3 letters
               |                #or
                   [A-Z]{2}     #two letters
                   \d{1,3}      #between 1 and 3 digits
                   [A-Z]?       #zero or one letters
               )$
            """

finished = False

while not finished:
    car_registration = input("Please enter your car registration: ")
    if len(car_registration) == 0:
        finished = True
    else:
        if re.match(pattern,car_registration,re.VERBOSE):
            print("Valid car registration")
        else:
            print("Invalid car registration")
