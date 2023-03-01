![Holberton school logo](https://secure.meetupstatic.com/photos/event/b/c/5/6/highres_475548214.jpeg)

# AirBnB clone - The console

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

(If you don't remember a shell is a program that provides a command-line interface for interacting with the operating system and executing commands. It is a text-based user interface that allows users to enter commands and receive output directly in the terminal window.)

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object 

# command interpreter or console
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
#  how to start it:
In order to start the console, you must use the following command: ./console.py

# How to used:
- manage (create, update, destroy, etc) objects via a console / command interprete
- store and persist objects to a file (JSON file)
- Allowed commands: create, show, destroy, all (shows all), update, help, quit
### Example how to open:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Contact Info:

#### Git: dariomnalerio

#### Git: 4mmZ