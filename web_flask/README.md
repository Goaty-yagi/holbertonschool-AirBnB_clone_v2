# AirBnB clone - Web framework

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Practice Exercises](#practice-exercises)
- [Tests](#tests)

## Learning Objectives

This project is based on the learning objectives - see the [LEARNING_OBJECTIVES](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/LEARNING_OBJECTIVES.md) file for details.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
- All your CSS files should be in the styles folder
- All your images should be in the images folder
- You are not allowed to use !important or id (#... in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on Chrome 56.0.2924.87.
- No cross browsers

## Practice Exercises

### 0. Hello Flask!

**File:** [0-hello_route.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/0-hello_route.py)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
- You must use the option strict_slashes=False in your route definition


### 1. HBNB

**File:** [1-hbnb_route.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/1-hbnb_route.py)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
 -- /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition


### 2. C is fun!

**File:** [2-c_route.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/2-c_route.py)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
 -- /hbnb: display “HBNB”
 -- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
- You must use the option strict_slashes=False in your route definition


### 3. Python is cool!

**File:** [3-python_route.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/3-python_route.py)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
 -- /hbnb: display “HBNB”
 -- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
 -- /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  --- The default value of text is “is cool”
- You must use the option strict_slashes=False in your route definition


### 4. Is it a number?

**File:** [4-number_route.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/4-number_route.py)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
 -- /hbnb: display “HBNB”
 -- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
 -- /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  --- The default value of text is “is cool”
 -- /number/<n>: display “n is a number” only if n is an integer
- You must use the option strict_slashes=False in your route definition


### 5. Number template

**File:** [5-number_template.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/5-number_template.py)<br>
[5-number.html](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/templates/5-number.html)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
 -- /hbnb: display “HBNB”
 -- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
 -- /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  --- The default value of text is “is cool”
 -- /number/<n>: display “n is a number” only if n is an integer
 -- /number_template/<n>: display a HTML page only if n is an integer:
  --- H1 tag: “Number: n” inside the tag BODY
- You must use the option strict_slashes=False in your route definition


### 6. Odd or even?

**File:** [6-number_odd_or_even.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/6-number_odd_or_even.py)<br>
[6-number_odd_or_even.html](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/templates/6-number_odd_or_even.html)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
 -- /: display “Hello HBNB!”
 -- /hbnb: display “HBNB”
 -- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
 -- /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
  --- The default value of text is “is cool”
 -- /number/<n>: display “n is a number” only if n is an integer
 -- /number_template/<n>: display a HTML page only if n is an integer:
  --- H1 tag: “Number: n” inside the tag BODY
 -- /number_odd_or_even/<n>: display a HTML page only if n is an integer:
  --- H1 tag: “Number: n is even|odd” inside the tag BODY
- You must use the option strict_slashes=False in your route definition

### 7. Improve engines

**File:** [file_storage](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/models/engine/file_storage.py)<br>
[db_storage.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/models/engine/db_storage.py)<br>
[state.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/models/state.py)<br>
**Description:** Update some part of our engine:<br>
**Requirement:** <br>
- Update FileStorage: (models/engine/file_storage.py)
 -- Add a public method def close(self):: call reload() method for deserializing the JSON file to objects

- Update DBStorage: (models/engine/db_storage.py)
 -- Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session tips

- Update State: (models/state.py) - If it’s not already present
 -- If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State

### 8. List of states

**File:** [7-states_list.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/7-states_list.py)<br>
[7-states_list.html](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/templates/7-states_list.html)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request you must remove the current SQLAlchemy Session:
 -- Declare a method to handle @app.teardown_appcontext
 -- Call in this method storage.close()
- You must use the option strict_slashes=False in your route definition
- Routes:
 -- /states_list: display a HTML page: (inside the tag BODY)
  --- H1 tag: “States”
  --- UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
    ---- LI tag: description of one State: <state.id>: <B><state.name></B>


### 9. Cities by states

**File:** [8-cities_by_states.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/8-cities_by_states.py)<br>
[8-cities_by_states.html](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/web_flask/templates/8-cities_by_states.html)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- To load all cities of a State:
 -- If your storage engine is DBStorage, you must use cities relationship
 -- Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session:
 -- Declare a method to handle @app.teardown_appcontext
 -- Call in this method storage.close()
- You must use the option strict_slashes=False in your route definition
- Routes:
 -- /states_list: display a HTML page: (inside the tag BODY)
  --- H1 tag: “States”
  --- UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
    ---- LI tag: description of one State: <state.id>: <B><state.name></B>


### 10. States and State

**File:** [8-cities_by_states.py](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/8-cities_by_states.py)<br>
[8-cities_by_states.html](https://github.com/Goaty-yagi/holbertonschool-AirBnB_clone_v2/tree/main/web_flask/web_flask/templates/8-cities_by_states.html)<br>
**Description:** Write a script that starts a Flask web application.<br>
**Requirement:** <br>
- Your web application must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
- To load all cities of a State:
 -- If your storage engine is DBStorage, you must use cities relationship
 -- Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session:
 -- Declare a method to handle @app.teardown_appcontext
 -- Call in this method storage.close()
- You must use the option strict_slashes=False in your route definition
- Routes:
 -- /states: display a HTML page: (inside the tag BODY)
  --- H1 tag: “States”
  --- UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
   ---- LI tag: description of one State: <state.id>: <B><state.name></B>
 -- /states/<id>: display a HTML page: (inside the tag BODY)
  --- If a State object is found with this id:
   ---- H1 tag: “State: ”
   ---- H3 tag: “Cities:”
   ---- UL tag: with the list of City objects linked to the State sorted by name (A->Z)
    ----- LI tag: description of one City: <city.id>: <B><city.name></B>
  --- Otherwise:
   ---- H1 tag: “Not found!”
- You must use the option strict_slashes=False in your route definition
