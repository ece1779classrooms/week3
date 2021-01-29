

import datetime  #package includes functions that provide day and time info

from flask import Flask
app = Flask(__name__)

@app.route('/time')
def example1():
    
    # use the datetime python module to obtain the current time
    # and store it in variable "time"
    time = 0
    

    response = """<!DOCTYPE html>
                  <html>
                      <p>
                        Current Date and Time: {}
                      </p>
                      <a href="/time">Refresh</a>
                  </html>
                  """

    return response.format(time)



app.run(host='0.0.0.0')