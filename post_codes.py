#post code validtor

import re

pattern = """
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
                [A-Z]{2}            #two letters
            """

finished = False

while not finished:
    post_code = input("Please enter your post code: ")
    if len(post_code) == 0:
        finished = True
    else:
        if re.match(pattern,post_code,re.VERBOSE):
            print("Valid post code")
        else:
            print("Invalid post code")
