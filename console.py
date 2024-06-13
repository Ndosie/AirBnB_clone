#!/usr/bin/python3
"""Defines HBNBCommand console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Defines hbnb command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Handle quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Handle EOF signal to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
