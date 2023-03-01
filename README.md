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

## The console main file
- **`console.py`** : contains the entry point of the command interpreter and specific methods to handle the input. **These are the commands you must use to work in the console**:

	| Function | Description | Usage example |
	| -- | -- | -- |
	| `do_quit` | To exit the program | `quit` |
	| `do_EOF` | To exit the program handling End of File (ctrl + D) | ctrl + D |
	| `emptyline` | Do nothing | empty line + enter |
	| `do_create` | Creates a new instance | `create BaseModel` |
	| `do_show` | Prints the string representation of an instance | `show Place a1c42567-c2b9-43bc-9825-9b2edffb483g` |
	| `do_destroy` | Deletes an instance based on the class name and id | `destroy User a1c42567-c2b9-43bc-9825-9b2edffb483f` |
	| `do_all` | Prints all string representation of all instances | `all` or `all Review`|
	| `do_update` | Updates an instance based on the class name and id by adding or updating attribute | `update User a1c42567-c2b9-43bc-9825-9b2edffb483f email "aibnb@mail.com"`|
	
# Usage:

## How to open
```
$ ./console.py
```


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

- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Serialize and deserialize objects (to and from a JSON file)
- Commands: create, show, destroy, all (shows all), update, help, quit

### Contact Info:

#### Git: dariomnalerio

#### Git: 4mmZ