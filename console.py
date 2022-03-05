#!/usr/bin/python3
" The console "

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage
import re


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


def isnumber(num):
    """
    This functions check is num is int,
    float or string and return it
    """
    try:
        if num.isdigit() is True:  # verify if num is a str
            num = int(num)
        else:
            num = float(num)  # try to convert to float
        return num
    except ValueError:
        return str(num)


class HBNBCommand(cmd.Cmd):
    """The console prompt"""

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """
        Exits console
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Usage: $ create ClassName
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")

        else:
            if args[0] in classes:
                instance = classes[args[0]]()
                print(instance.id)
                instance.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation
        Usage: $ show ClassName id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in classes:
                if len(args) > 1:
                    store = storage.all()
                    key = args[0] + "." + args[1]

                    for a, b in store.items():
                        if a == key:
                            print(b)
                            return
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Usage: $ destroy ClassName 1234-1234-1234
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")

        else:
            if args[0] in classes:
                if len(args) > 1:
                    store = storage.all()
                    key = args[0] + "." + args[1]
                    if key in store.keys():
                        # for i in store.keys():
                        #    if i == key:
                        del store[key]
                        storage.save()
                        return
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: $ all ClassName or $ all
        """
        args = arg.split()
        store = storage.all()
        new_list = []

        if len(args) == 0:
            for a in store.values():
                new_list.append(a.__str__())
            print(new_list)

        elif args[0] in classes:
            for a in store.values():
                if a.__class__.__name__ == args[0]:
                    new_list.append(a.__str__())
            print(new_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        store = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in classes:  # exist class name?
                if len(args) > 1:  # exit id?
                    if len(args) > 2:  # exist attribute name?
                        store = storage.all()
                        key = args[0] + "." + args[1]
                        if key in store.keys():
                            if len(args) > 3:  # exit attribute value?
                                args_re = args[3][1:-1]
                                args_re = isnumber(args_re)
                                setattr(store[key], args[2], args_re)
                                storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def default(self, arg):
        """
        retrieve all instances of a class
        Usage: <class name>.all()
        """
        args = arg.split(".")
        store = storage.all()

        if len(args) != 2 or args[0] not in classes:
            cmd.Cmd.default(self, arg)
        else:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                sum = 0
                for value in store.keys():
                    class_name = value.split(".")[0]
                    if class_name == args[0]:
                        sum += 1
                print(sum)
            elif 'show("' in args[1] and args[1][-1] == ")":
                index_start = args[1].find("(") + 2  # index where start the id
                index_end = args[1].find(")") - 1  # index where end the id
                id = args[1][index_start:index_end]
                self.do_show(args[0] + " " + id)

            else:
                cmd.Cmd.default(self, arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
