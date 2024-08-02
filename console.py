#!/usr/bin/python3
"""Defines HBNBCommand console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


def parse(arg):
    return arg.split()


class HBNBCommand(cmd.Cmd):
    """Defines hbnb command interpreter"""

    prompt = '(hbnb) '
    __classes = { 'BaseModel', 'User' }

    def emptyline(self):
        """Handles empty command to do nothing"""
        pass

    def do_quit(self, arg):
        """Handles quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Handles EOF signal to exit the program"""
        return True
    
    def do_create(self, arg):
        """Handles new instance creation"""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = parse(arg)
        o_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in o_dict:
            print("** no instance found **")
        else:
            print(o_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = parse(arg)
        o_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in o_dict:
            print("** no instance found **")
        else:
            del o_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                else:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        args = parse(arg)
        o_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in o_dict:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = o_dict["{}.{}".format(args[0], args[1])]
            for i in range(2, len(args), 2):
                try:
                    obj.__dict__[args[i]] = args[i + 1]
                except IndexError:
                    print("** value missing **")
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
