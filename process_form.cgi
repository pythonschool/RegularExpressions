#!/usr/local/bin/python3

import cgi

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

def get_booking_details():
    form_data = cgi.FieldStorage()
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

#main program
if __name__ == "__main__":
    try:
        html_top()
        first_name, last_name, street, town, postcode,phone, car, date_in, date_out = get_booking_details()
        print("{0}<br/>".format(first_name))
        print("{0}<br/>".format(last_name))
        print("{0}<br/>".format(street))
        print("{0}<br/>".format(town))
        print("{0}<br/>".format(postcode))
        print("{0}<br/>".format(phone))
        print("{0}<br/>".format(car))
        print("{0}<br/>".format(date_in))
        print("{0}<br/>".format(date_out))
        html_tail()
    except:
        cgi.print_exception()
