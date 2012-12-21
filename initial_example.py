#this program demonstrates simple use of regex

import re

pattern = "Ma?cNich?ol{1,2}"

finished = False

while not finished:
    last_name = input("Please enter your last name: ")
    if len(last_name) == 0:
        finished = True
    else:
        if re.match(pattern,last_name):
            print("Valid spelling for McNicol")
        else:
            print("Invalid spelling for McNicol")
