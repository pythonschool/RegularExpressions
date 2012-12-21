#car registration validtor

import re

pattern = "[A-Z](([A-Z]\d{2}|\d{1,3})[A-Z]{3}|[A-Z]{2}\d{1,3}[A-Z]?$)"

finished = False

while not finished:
    car_registration = input("Please enter your car registration: ")
    if len(car_registration) == 0:
        finished = True
    else:
        if re.match(pattern,car_registration):
            print("Valid car registration")
        else:
            print("Invalid car registration")
