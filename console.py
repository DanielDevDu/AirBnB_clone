#!/usr/bin/python3
" The console "

import cmd
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage

classes = {"BaseModel": BaseModel, "User": User}

class HBNBCommand(cmd.Cmd):
    """ The console prompt """
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        return False

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id """
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
        """ Prints the string representation of an instance based on the class name and id """
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
        """: Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        
        else:
            if args[0] in classes:
                if len(args) > 1:
                    store = storage.all()
                    key = args[0] + "." + args[1]
                    if key in store.keys():
                    #for i in store.keys():
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
        """ Prints all string representation of all instances 
        based or not on the class name. Ex: $ all BaseModel or $ all"""
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
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        store = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in classes: #exist class name?
                if len(args) > 1: #exit id?
                    if len(args) > 2: #exist attribute name?
                        store = storage.all()
                        key = args[0] + "." + args[1]
                        if key in store.keys():
                            if len(arg) > 3: #exit attribute value?
                                setattr(store[key], args[2], args[3])
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
