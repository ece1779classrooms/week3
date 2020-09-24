"""
    3rd Tutorial Session
"""

from flask import render_template, request
from app import webapp


@webapp.route('/collatz_form',methods=['GET'])
def collatz_form():

# student code starts here
    html = """
        <!DOCTYPE html>
        <head>
            <title>Collatz series</title>
        </head>
        <body>
            <form method='get' action='/collatz'>
                <label>N</label>
                    <input type='text' name='n'>
                <input type='submit' value='Show collatz series'>
            </form>
        <body>
    </html>
    """
    return html
#end of student code

