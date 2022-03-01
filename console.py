#!/usr/bin/python3
" The console "

import cmd

class HBNBCommand(cmd.Cmd):
    """ The console prompt """
    prompt = '(hbnb)'

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print ("hi,", person)
        else:
            print ('hi')

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
