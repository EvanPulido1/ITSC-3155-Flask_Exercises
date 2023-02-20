# Evan Pulido
# ITSC 3155
# Flask Exercise 1

# This program has to give a page that shows the current time.
# To run the program, open the terminal, then type:
# export FLASK_APP=current_time  then   flask run
# This gives link to page that shows current time

# Links that I used to get the current time(day, week, month, year, etc):
# https://www.programiz.com/python-programming/datetime/current-time
# https://favtutor.com/blogs/get-current-year-python#:~:text=The%20strfttime()%20function%20in,year%20of%20the%20date%20object.
# https://pythonexamples.org/python-datetime-get-day-of-month/
# https://www.itsolutionstuff.com/post/how-to-get-current-month-in-pythonexample.html
# https://pynative.com/python-get-the-day-of-week/#h-how-to-get-the-day-of-the-week-from-datetime-in-python
from datetime import datetime

# Link that I used to learn about how to use flask:
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def time():
    dt = datetime.now()

    # This gets the name of the weekday (Monday, Tuesday, etc)
    weekday = dt.strftime('%A')
    # This gets the current month (January, February, etc)
    month = dt.strftime('%B')
    # Gets the day of the current month (1, 2, 3, etc)
    day_number = dt.strftime('%d')
    # Gets the current year (it should be 2023)
    year = dt.strftime('%Y')
    # Gets the current time when the page is opened (only updates when you click refresh on the page)
    current_time = dt.strftime('%H:%M:%S')

    # Displays the current date time
    return 'The current date time is ' + weekday + ', ' + month + ' ' + day_number + ' ' + year + ' ' + current_time