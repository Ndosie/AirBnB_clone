#!/usr/bin/python3
"""Defines HBNBCommand console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines hbnb command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Handles empty command to do nothing"""
        pass

    def do_quit(self, arg):
        """Handles quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
