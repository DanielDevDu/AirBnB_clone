# AirBnB Clone - The Console 🚀
This is the first step towards building our first full web application: the AirBnB clone. The console is the first part of the AirBnB project at Holberton School. The goal of AirBnB project is to eventually develop our server as a simple copy of the AirBnB Website.

## Functions of the Console 💻
* Create a new object (ex: a new User or a new City).
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…).
* Update attributes to the classes.Update attributes of an object.
* Destroy an object.

## Table of Content 📋
* [Version](#Version)
* [Installation](#installation)
* [Commands](#Commands)
* [Usage](#usage)
* [Folders](#folders)
* [Files](#files)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Version ✅
This project is interpreted, tested and created on Ubuntu 20.04.3 LTS using python3 (version 3.8.10)

## Installation 😎
* Clone this repository to your local machine with the command: `git clone "https://github.com/Daniel13713/AirBnB_clone.git"`.
* Access the AirBnb directory: `cd AirBnB_clone`.
* Run the console (interactive mode): `./console` and press enter to access the console.
* Run the console (non-interactive mode): `echo "<command>" | ./console.py`.

## Commands 🪀

| COMMAND | DESCRIPTION |
| ----- | ------------ |
| quit | Exits the program  |
| EOF | Exits the program  |
| help | Description to function  |
| ENTER | Overwrites default emptyline and does nothing  |
| create | Creates a new instance, saves it (to the JSON file) and prints the id |
| show | Prints the string representation of an instance by it's name and id (id required)|
| destroy | Deletes an instance by it's name and id (id required) (saves the changes into the JSON file) |
| all |  Prints all string representation of all instances |
| update | Updates an instance by it's name and id, adding or updating attributes (saves the changes into the JSON file) |

## Usage ⌨️

```
annie@DESKTOP-KMANJKQ:~/AirBnB_clone$ ./console.py 
```

```
(hbnb)create BaseModel
9f0c435d-d650-4c89-b450-7ef24025e693
(hbnb)
```

```
(hbnb) all MyModel
** class doesn't exist **
(hbnb)
```

```
(hbnb)all BaseModel
["[BaseModel] (9f0c435d-d650-4c89-b450-7ef24025e693) {'id': '9f0c435d-d650-4c89-b450-7ef24025e693', 'created_at': datetime.datetime(2022, 3, 4, 6, 14, 25, 310677), 'updated_at': datetime.datetime(2022, 3, 4, 6, 14, 25, 310746)}"]
(hbnb)
```

```

(hbnb)show BaseModel 9f0c435d-d650-4c89-b450-7ef24025e693
[BaseModel] (9f0c435d-d650-4c89-b450-7ef24025e693) {'id': '9f0c435d-d650-4c89-b450-7ef24025e693', 'created_at': datetime.datetime(2022, 3, 4, 6, 14, 25, 310677), 'updated_at': datetime.datetime(2022, 3, 4, 6, 14, 25, 310746)}
(hbnb)
```

```

(hbnb)update BaseModel 9f0c435d-d650-4c89-b450-7ef24025e693 first_name "Betty"
(hbnb)
```

```

(hbnb)show BaseModel 9f0c435d-d650-4c89-b450-7ef24025e693
[BaseModel] (9f0c435d-d650-4c89-b450-7ef24025e693) {'id': '9f0c435d-d650-4c89-b450-7ef24025e693', 'created_at': datetime.datetime(2022, 3, 4, 6, 14, 25, 310677), 'updated_at': datetime.datetime(2022, 3, 4, 6, 14, 25, 310746), 'first_name': '"Betty"'}
(hbnb)
```

```

(hbnb)destroy BaseModel 9f0c435d-d650-4c89-b450-7ef24025e693
(hbnb)
```

```

(hbnb)show BaseModel 9f0c435d-d650-4c89-b450-7ef24025e693
** no instance found **
(hbnb)
```

## Folders 📁

| FOLDERS | DESCRIPTION |
| ----- | ------------ |
| models | Contains all the classes that are inherit from basemodel |
| engine | Contains the file store engine |
| tests | Tests cases to the all the proyect using unit tests |
| AUTHORS | Listing all individuals having contributed content to the repository (File)|
| README.md | General description of the project (File)|
| console.py | Command line interpreter (File)|

## Files 🗂️

| FILES | DESCRIPTION |
| ----- | ------------ |
| base_model.py | Defines all common attributes and methods |
| __init__.py | Python packages |
| file_storage.py | Storage engine |
| user.py | User class inherits from basemodel |
| state.py | State class inherits from basemodel |
| city.py | City class inherits from basemodel |
| amenity.py | Amenity class inherits from basemodel |
| place.py | Place class inherits from basemodel |
| review.py | Review class inherits from basemodel |


