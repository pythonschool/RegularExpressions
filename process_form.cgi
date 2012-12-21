#!/usr/local/bin/python3

import cgi, re

def html_top():
    print("""Content-type:text/html\n\n
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8"/>
            </head>
            <body>""")

def html_tail():
    print("""    </body>
    </html>""")

def get_booking_details(form_data):
    first_name = form_data.getvalue("first_name")
    last_name = form_data.getvalue("last_name")
    street = form_data.getvalue("street")
    town = form_data.getvalue("town")
    postcode = form_data.getvalue("postcode")
    phone = form_data.getvalue("phone")
    car = form_data.getvalue("car")
    date_in = form_data.getvalue("date_in")
    date_out = form_data.getvalue("date_out")
    return first_name, last_name,street, town, postcode, phone, car, date_in, date_out

def validate_form_field(field,regex):
    if re.match(regex,field,re.VERBOSE):
        return True
    else:
        return False

def validate_post_code(post_code):
    regex = """
                [A-Z]               #a single letter
                                    #followed by either:
                    (                   
                    [A-Z]           #an another letter
                                    #and either:
                        (
                        \d{1,2}     #one or two numbers
                        |           #or
                        \d[A-Z]     #a single number followed by a single letter
                        )   
                    |               #or
                    \d{1,2}         #one or two numbers
                    )
                \s\d                #space followed by a single number
                [A-Z]{2}$            #two letters
            """
    return validate_form_field(post_code,regex)

def validate_telephone_number(phone):
    regex = """\(0                   #open bracket followed by a zero
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
    return validate_form_field(phone,regex)

def validate_car_registration(car):
    regex = """
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

    return validate_form_field(car,regex)

def create_form(first_name="", last_name="",
                street="", town="", postcode="",phone="",
                car="", date_in="", date_out="",
                post_code_valid="",phone_valid="",car_valid=""):
    validation_indicators = []
    for validation in [post_code_valid,phone_valid,car_valid]:
        if validation == False:
            validation_indicators.append("Invalid")
        else:
            validation_indicators.append("")
    
    form = """
            <form method="post" action="process_form.cgi">
            <h1>Car Park Booking Form</h1>
            First name: <input type="text" name="first_name" placeholder="e.g. John" value="{0}" /><br/>
            Last name: <input type="text" name="last_name" placeholder="e.g. Bain" value="{1}"/><br/>
            Street address: <input type="text" name="street" placeholder="e.g. 5 Ormond Way" value="{2}"/><br/>
            Town: <input type="text" name="town" placeholder="e.g. Dunkeld" value="{3}"/><br/>
            Post code: <input type="text" name="postcode" placeholder="e.g. PH15 6SJ" value="{4}"/>{9}<br/>
            Telphone number: <input type="tel" name="phone" placeholder="e.g. (01123) 438672" value="{5}"/>{10}<br/>
            Car registration: <input type="text" name="car" placeholder="e.g. SJ10SPL" value="{6}"/>{11}<br/>
            <br />
            Date in: <input type="date" name="date_in" placeholder="e.g. 2012-12-20" value="{7}"/><br/>
            Date out: <input type="datetime" name="date_out" placeholder="e.g. 2012-12-28" value="{8}"/><br/>
            <br/>
            <input type="submit" name="submit" value="Submit Booking"/>
                        </form>
            """.format(first_name, last_name,
                street, town, postcode,phone,
                car, date_in, date_out,
                validation_indicators[0], validation_indicators[1], validation_indicators[2])
    return form


#main program
if __name__ == "__main__":
    try:
        html_top()
        form_data = cgi.FieldStorage()
        #find out if there is anything in the post variable
        if len(form_data.keys()) > 0:
            #pre-existing form
            first_name, last_name, street, town, postcode,phone, car, date_in, date_out = get_booking_details(form_data)
            #validate 
            post_code_valid = validate_post_code(postcode)
            phone_valid = validate_telephone_number(phone)
            car_valid = validate_car_registration(car)
            if post_code_valid and phone_valid and car_valid:
                form = "Your booking has been successful!"
            else:
                #generate form to show invalid data
                form = create_form(first_name, last_name,
                    street, town, postcode,phone,
                    car, date_in, date_out,
                    post_code_valid,phone_valid,car_valid)
        else:
            #new blank form
            form = create_form()       
        print(form)
        html_tail()
    except:
        cgi.print_exception()
