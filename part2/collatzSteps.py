"""
    2nd Tutorial Session
    
    How to run this app:
    
    Option 1:

    1. Starting your web application -> From the menu on the top click 'Window' and then click 'New Terminal'
    2. Go the directory where the collatzSteps.py file is
    3. Type: python collatzSteps.py
    
    Option 2: Click the green run button.
    
    
    Instructions:

    1. Use the request object to get the number passed in via the url. Make sure to validate that the input is an integer or throw an error.
    2. Using the input integer compute and return the Collatz steps.
    2. Create a simple html snippet and it back to the user that shows the collantz steps for a given integer(See part2.jpg for what your output should look like, if you provided a value of 5)
    3. Find the public ip of your instance by using the following command: dig +short myip.opendns.com @resolver1.opendns.com
    3. You can see your webpage at the following example url (replace this ip with the one you got from step 3) http://3.231.155.231:5000/collatz?n=5 


    
"""

import datetime
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/collatz')
def collatz():
    """
    Create a web page with the number of steps it takes to reach 1, by applying 
    the two steps of the Collatz conjecture beginning from n.

    """

# student code starts here

    if request.args.get('n').isdigit() == False:
        return "Error! All inputs most be of type int"

    n = original = int(request.args.get('n'))
    
    steps = []
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps.append(n)

    series = str(original)

    for i in steps:
        series = series + "->" + str(i)

    html = """
        <!DOCTYPE html >
            <body>
                <p>Collantz series for {0} </p>
                <p>{1}</p>
                <p>Number of steps = {2}</p>
            </body>
        </html>
    """

    return html.format(original,series,len(steps))

#end of student code

app.run(host='0.0.0.0')
    

