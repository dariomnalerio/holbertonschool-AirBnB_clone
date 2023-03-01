![Holberton school logo](https://secure.meetupstatic.com/photos/event/b/c/5/6/highres_475548214.jpeg)

# AirBnB clone - The console

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

(If you don't remember a shell is a program that provides a command-line interface for interacting with the operating system and executing commands. It is a text-based user interface that allows users to enter commands and receive output directly in the terminal window.)

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object 

# Requirements

- All the files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All the files use the pycodestyle (version 2.7.) standard guidelines, including class and functions documentation
- All tests are execute using the unittest module

# command interpreter or console

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

# Usage:

## How to open
```
$ ./console.py
(hbnb) help

## Usage examples
### Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_create
create BaseModel
$
$ cat test_create | ./console.py
(hbnb)cac68aef-e8eb-4379-8981-b6809ba01b72
$
```

### Interactive mode

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
(hbnb) create BaseModel
c384e626-0924-4fd7-910c-2b87af45215c
(hbnb) 
(hbnb) all
["[BaseModel] (c384e626-0924-4fd7-910c-2b87af45215c) {'id': 'c384e626-0924-4fd7-910c-2b87af45215c', 'created_at': datetime.datetime(2022, 10, 15, 15, 12, 22, 529850), 'updated_at': datetime.datetime(2022, 10, 15, 15, 12, 22, 529862)}"]
(hbnb)
(hbnb) destroy BaseModel c384e626-0924-4fd7-910c-2b87af45215c
(hbnb) show BaseModel c384e626-0924-4fd7-910c-2b87af45215c
** no instance found **
(hbnb)
(hbnb) quit
$
```

- manage (create, update, destroy, etc) objects via a console / command interprete
- store and persist objects to a file (JSON file)
- Allowed commands: create, show, destroy, all (shows all), update, help, quit

### Contact Info:

#### Git: dariomnalerio

#### Git: 4mmZ