# Flask Workshop 
This repository contains files that were created during a workshop by hackAD given on February 16, 2020 by [Nav](https://www.github.com/navyasuri). 

### Setup and Boilerplate
The workshop code used [this boilerplate](https://github.com/navyasuri/flask-boilerplate) for Flask - a very barebones boilerplate that only provides a basic file structure. Feel free to use both the boilerplate and the current project to experiment with Flask

### Goal of the Project
The project serves as a very simple demonstration into how the Flask framework operates. Since the workshops was intended for beginners who are primarily new to web development, the project setup and working is rather simple. The project takes in grades in the form of decimals in a `<textarea>` element and the user's email. The user posts this data to the server, where it is processed and a grade report (an average grade) is sent to the user's email. 

## What the Flask
Flask is a micropython framework commonly used to make web-apps. You can read more about it [here](https://flask.palletsprojects.com/en/1.1.x/). Follow along with the installation guide to get Flask set-up based on your current Operating System, and this repository should work as long as Flask is set up. 

### Basics of flask
- **Routes**: These are specified with the `@app.route` decorator. Each route defines a new page. 
- **Methods**: In this app we use `POST` and `GET` methods. They are specified in the second argument of `@app.route()`. Futher information can be found [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods)
- **Templates**: Flask uses HTML templates alongside a template engine known as Jinja. The workshop did not go over rendering templates with varaibles. Read more [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates)
- **`request`**: The posted form data can be accessed using the `request` object. `request.form` is an Immutable Dictionary with the form data. 
- **Static Files**: To serve static files, such as stylesheets, js files or images and other content, we store the files in the `static` directory. To access these files, use the `url_for()` method as described [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files)
Note: In this project, we have created a `utils` directory where the mailing script resides. 

### Client-Server Architecure
Flask is essentially a web server. It can interface a database and do much more than the scope of the workshop. The user's browser acts a client and the flask app is a server. 
![Client-Server picture](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Client-server-model.svg/1200px-Client-server-model.svg.png)

### Web-app structure
The web app here consists of just 2 routes, one which takes in the data via an HTML form from the user, and the other displays the result as a string. Note that after adding in the mailing script, it is just as easy to send the user back to the same page to enter more data after the user submits the grade (making this a single page web app)

### Setting up the emailing script
Make a new file in the `utils` directory called `emailconfig.py`. The contents of the file should be 
```
EmailAddress = "your-email-address"
Password = "your-password"
```
Once this is set up, you should be able to send out emails by calling the function defined in `utils/mailing.py`. 

### Thank you!
Thank you for reading this. For more, refer to [flask documentation](https://flask.palletsprojects.com/en/1.1.x/), and if you still have questions, do not hesitate to reach out. Cheers!


