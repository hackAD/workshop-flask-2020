from flask import Flask, request, render_template, url_for
import os
import utils.mailing

# To run this, type in terminal: `export FLASK_APP=main.py` (or whatever name of file is)
# Then type flask run
# Additional options: Use `flask run --host=0.0.0.0` or any other host you want to specify.
# additionally you can add `--port=4000` after the previous command to run on port 4000
app = Flask(__name__)

# What to do when user goes to default route
@app.route('/')
def show_home(): # The function name can be anything

    # You can just return default text 
    # return "Hello. Welcome to default page"

    # You'd rather return a rendered html file
    return render_template("index.html") 

# Just another route - this will be 0.0.0.0:4000/other
@app.route('/calculated', methods=['POST'])
def show_another():

    print(request.form)
    print(request.form["grades"])
    grades = request.form["grades"].split("\r\n")
    grade_values = []

    try:
        for grade in grades:
            grade_values.append(float(grade))
    except:
        return "Sorry, we do not support strings"
    
    avg = sum(grade_values)/len(grade_values)
    # Send email
    utils.mailing.email(request.form["email"], "Your grade is "+str(avg))

    return "Your average grade point is "+str(avg)
