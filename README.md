# HolbertonBnB
An Airbnb clone
![AIRBNB](assets/airbnb.png)

## ***Description***
HolbertonBnB is a complete RESTful web application, integrating file and database (MySQL) storage in a back-end API with front-end interfacing in a clone of AirBnB. The front-end is designed using HTML5/CSS3 and is served using Python Flask.

![an image of the project architecture](assets/console.png)

## ***Classes***

HolbertonBnB supports the following classes:
- BaseModel
- User
- Place
- Review
- State
- City
- Amenity

## ***Storage***
There are two abstracted storage engines that help in saving classes informations - FileStorage and DBStorage.

### File Storage
In `FileStorage` mode, every time the backend is initialized, HolbertonBnB instantiates an instance of `FileStorage` called `storage`. The storage object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instances are created, updated, or deleted, the `storage` object is used to save changes in the `file.json`.

## ***Console***
The Console is a command line interpreter that permits management of the backend of HolbertonBnB.
It allows the creation, update and deletion of instances that are reloaded from storage.

### help
Typing help into the command will display the available commands that you can use and know their utility.
```
-Welcome to the HBNB CLI Interface-

(hbnb)help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```
### quit and EOF
Typing either quit or EOF wil exit the console.
```
-Welcome to the HBNB CLI Interface-

(hbnb) quit
Thanks for using Hbnb Console
```
```
-Welcome to the HBNB CLI Interface-

(hbnb) EOF
Thanks for using Hbnb Console
```
### create
- Usage: `create <class>`
Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json
```
-Welcome to the HBNB CLI Interface-

(hbnb) create BaseModel
6933b35e-e4f6-4601-bde9-f424841e132e
```

### show
- Usage: `show <class> <id>`
Prints the string representation of a class instance based on a given id.
```
-Welcome to the HBNB CLI Interface-

(hbnb) create BaseModel
7c3c78d2-c571-4584-a3dd-068b05783e4a
(hbnb) show BaseModel 7c3c78d2-c571-4584-a3dd-068b05783e4a
[BaseModel] (7c3c78d2-c571-4584-a3dd-068b05783e4a) {'id': '7c3c78d2-c571-4584-a3dd-068b05783e4a', 'created_at': datetime.datetime(2022, 6, 30, 13, 47, 41, 740966), 'updated_at': datetime.datetime(2022, 6, 30, 13, 47, 41, 740996)}
```

### destroy
- Usage: `destroy <class> <id>`
Deletes a class instance based on a given id.
```
-Welcome to the HBNB CLI Interface-

(hbnb) create BaseModel
74e2a502-d5af-4b87-bf21-aae46f92e5ca
(hbnb) show BaseModel 74e2a502-d5af-4b87-bf21-aae46f92e5ca
[BaseModel] (74e2a502-d5af-4b87-bf21-aae46f92e5ca) {'id': '74e2a502-d5af-4b87-bf21-aae46f92e5ca', 'created_at': datetime.datetime(2022, 6, 30, 13, 52, 2, 702820), 'updated_at': datetime.datetime(2022, 6, 30, 13, 52, 2, 702851)}
(hbnb) destroy BaseModel 74e2a502-d5af-4b87-bf21-aae46f92e5ca
(hbnb) show BaseModel 74e2a502-d5af-4b87-bf21-aae46f92e5ca
** no instance found **
```

### all
- Usage: `all` or `all <class>`
Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.
```
-Welcome to the HBNB CLI Interface-

(hbnb) all
["[BaseModel] (6933b35e-e4f6-4601-bde9-f424841e132e) {'id': '6933b35e-e4f6-4601-bde9-f424841e132e', 'created_at': datetime.datetime(2022, 6, 30, 13, 40, 52, 68310), 'updated_at': datetime.datetime(2022, 6, 30, 13, 40, 52, 68346)}", "[BaseModel] (7c3c78d2-c571-4584-a3dd-068b05783e4a) {'id': '7c3c78d2-c571-4584-a3dd-068b05783e4a', 'created_at': datetime.datetime(2022, 6, 30, 13, 47, 41, 740966), 'updated_at': datetime.datetime(2022, 6, 30, 13, 47, 41, 740996)}", "[BaseModel] (4a1d069c-bced-48a1-827d-03f2c2447927) {'id': '4a1d069c-bced-48a1-827d-03f2c2447927', 'created_at': datetime.datetime(2022, 6, 30, 13, 51, 7, 254570), 'updated_at': datetime.datetime(2022, 6, 30, 13, 51, 7, 254599)}", "[BaseModel] (49804e1a-c69b-467b-8c89-2bb3fae1e332) {'id': '49804e1a-c69b-467b-8c89-2bb3fae1e332', 'created_at': datetime.datetime(2022, 6, 30, 13, 51, 43, 142791), 'updated_at': datetime.datetime(2022, 6, 30, 13, 51, 43, 142823)}"]
```

### update
Usage: `update <class> <id> <attribute name> <attribute value>` 
The attribute value should be between double quotes if it is a string
Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at).
```
-Welcome to the HBNB CLI Interface-

(hbnb) all
["[BaseModel] (6933b35e-e4f6-4601-bde9-f424841e132e) {'id': '6933b35e-e4f6-4601-bde9-f424841e132e', 'created_at': datetime.datetime(2022, 6, 30, 13, 40, 52, 68310), 'updated_at': datetime.datetime(2022, 6, 30, 13, 40, 52, 68346)}", "[BaseModel] (7c3c78d2-c571-4584-a3dd-068b05783e4a) {'id': '7c3c78d2-c571-4584-a3dd-068b05783e4a', 'created_at': datetime.datetime(2022, 6, 30, 13, 47, 41, 740966), 'updated_at': datetime.datetime(2022, 6, 30, 13, 47, 41, 740996)}", "[BaseModel] (4a1d069c-bced-48a1-827d-03f2c2447927) {'id': '4a1d069c-bced-48a1-827d-03f2c2447927', 'created_at': datetime.datetime(2022, 6, 30, 13, 51, 7, 254570), 'updated_at': datetime.datetime(2022, 6, 30, 13, 51, 7, 254599)}", "[BaseModel] (49804e1a-c69b-467b-8c89-2bb3fae1e332) {'id': '49804e1a-c69b-467b-8c89-2bb3fae1e332', 'created_at': datetime.datetime(2022, 6, 30, 13, 51, 43, 142791), 'updated_at': datetime.datetime(2022, 6, 30, 13, 51, 43, 142823)}"]
(hbnb) update BaseModel 49804e1a-c69b-467b-8c89-2bb3fae1e332 NAME "Jack Smith"
(hbnb) show BaseModel 49804e1a-c69b-467b-8c89-2bb3fae1e332 
[BaseModel] (49804e1a-c69b-467b-8c89-2bb3fae1e332) {'id': '49804e1a-c69b-467b-8c89-2bb3fae1e332', 'created_at': datetime.datetime(2022, 6, 30, 13, 51, 43, 142791), 'updated_at': datetime.datetime(2022, 6, 30, 14, 32, 34, 845642), 'NAME': 'Jack Smith'}
```

## ***Testing***
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:
```
$ python3 unittest -m discover tests
```
Also, you can specify a single test file to run at a time:
```
$ python3 unittest -m tests/test_base_model.py
```

## ***Authors***
Youssef Abid <[Yousseffabid](https://github.com/yousseffabid)>
Youssef Jallouli <[Youssef J](https://github.com/YoussefJell)>
