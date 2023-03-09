# Evan Pulido
# ITSC 3155
# Flask Exercise 2

# Links that I used to help me write code for this:
# https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html

# This imports flask and multiple other modules
from flask import Flask, request, render_template
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application which URL is associated function
@app.route('/', methods =["GET", "POST"])
def form():
    if request.method == "POST":
       # getting input with number = integer in HTML form
       value = request.form.get("integer")

       # Creates a title for the Calculate page
       title = f'<h1>Calculate</h1>'
       # Creates a hyperlink to the home page
       page = f'<a href= http://127.0.0.1:5000>Go home</a>'

       # Link I used to learn about isdigit:
       # https://www.tutsmake.com/python-check-whether-a-string-contains-number-or-letter/
       # If what the user inputs in the box is a number, this will take the user to a new 
       # page telling them if the value is odd, even, not an integer, or if there was no value inputted
       if value.isdigit():
          if (int(value) % 2) == 0:
             return title + value + ' is even' + f'<br>' + f'<br>' + page
          else:
             return title + value + ' is odd' + f'<br>' + f'<br>' + page
       else:
          if value == '':
             return title + 'No number provided!' + f'<br>' + f'<br>' + page
          else:
             return title + value + ' is not an integer!' + f'<br>' + f'<br>' + page
    
    return render_template("form.html")
 
if __name__=='__main__':
   app.run()