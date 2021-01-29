

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

    n = 

#end of student code

    
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
                <p>Collatz series for {0} </p>
                <p>{1}</p>
                <p>Number of steps = {2}</p>
            </body>
        </html>
    """

    return html.format(original,series,len(steps))


app.run(host='0.0.0.0')
    

