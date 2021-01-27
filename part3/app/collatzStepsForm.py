"""
    3rd Tutorial Session
"""

from flask import render_template, request
from app import webapp


@webapp.route('/collatz_form',methods=['GET'])
def collatz_form():

    html = """
        <!DOCTYPE html>
        <head>
            <title>Collatz series</title>
        </head>
        <body>
            <form method='get' action='/collatz'>
            
            <!-- student code starts here -->

                <label>N</label>
                    <input type='text' name='n'>
                <input type='submit' value='Show collatz series'>

            <!-- end of student code -->


            </form>
        <body>
    </html>
    """
    return html

