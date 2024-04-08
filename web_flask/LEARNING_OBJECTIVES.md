# Learning Objectives

- [What is a Web Framework](#What-is-a-Web-Framework)
- [How to build a web framework with Flask](#How-to-build-a-web-framework-with-Flask)
- [How to define routes in Flask](#How-to-define-routes-in-Flask)
- [What is a route](#What-is-a-route)
- [How to handle variables in a route](#How-to-handle-variables-in-a-route)
- [What is a template](#What-is-a-template)
- [How to create a HTML response in Flask by using a template](#How-to-create-a-HTML-response-in-Flask-by-using-a-template)
- [How to create a dynamic template (loops, conditions...)](#How-to-create-a-dynamic-template-(loops, conditions...))
- [How to display in HTML data from a MySQL database](#How-to-display-in-HTML-data-from-a-MySQL-database)

## What is a Web Frame Work?
 a web framework facilitates the process of building web applications by providing a structured set of tools, libraries, and conventions. 
Key features

- Http request and response
- Routing 

## How to build APP with Flask?
### 1, Setup environment:
*  Install Flask `pip install Flask`

### 2, Create Project Structure:
- Create a new directory for your Flask project.
- Inside the project directory, create a Python script (e.g., app.py) to define your Flask application.
- Optionally, create subdirectories for templates, static files, and other resources.

### 3, Define Flask Application:
- Import the Flask class from the flask module.
- Create an instance of the Flask class to represent your application.
- Define routes and view functions to handle different URLs and HTTP methods.

```python
# app.py

from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

# Define route and view function
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello/<name>') # html file
def hello(name):
    return render_template('hello.html', name=name)

# Run Flask development server
if __name__ == '__main__':
    app.run(debug=True)

```

## How to define routes in Flask

use the decorator app.route like above.

## What is route

Route is a specific URL pattern associated with a view function.

## How to handle variables in a route
you can handle variables in a route by defining dynamic route parameters.
```python
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

# Define another route with multiple dynamic parameters
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'The sum of {num1} and {num2} is {num1 + num2}'
```

## What is a template
a template refers to a file containing a pre-designed structure that defines the layout and appearance of a web page. 

## How to create a HTTP response in Flask by using a template]
* 1, create template
```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>

```
* 2, import render_template
* 3, return render_template with attributes

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home', heading='Welcome!', content='This is the homepage.')

if __name__ == '__main__':
    app.run(debug=True)
```

## How to create a dynamic template (loops and conditions)
For loops and conditions, start with {% %} and end with {% endfor %} or {% endif %}
```html
<ul>
    {% for user in users %}
        <li>{{ user.username }}</li>
    {% endfor %}
</ul>
{% if users %}
    <p>There are {{ users|length }} users.</p>
{% else %}
    <p>No users found.</p>
{% endif %}
```
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def users():
    # Dummy user data for demonstration
    users = [
        {'username': 'Alice'},
        {'username': 'Bob'},
        {'username': 'Charlie'}
    ]
    return render_template('dynamic.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

```
## How to display data in HTMl from MySQL database
Get data from database, then pass it to the template