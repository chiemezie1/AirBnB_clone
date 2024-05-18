#!/usr/bin/python3
"""AirBnB_clone Console Module"""

import cmd


import models

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for AirBnB Clone

    Attributes:
        prompt (str): command prompt prefix string
        cmd (Cmd): command line interpreter
        Models (dict): dictionary of available models
    """
    prompt = "(hbnb) "
    cmd = cmd.Cmd()

    Models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of Available Models and saves it to JSON file"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.Models:
            print("** class doesn't exist **")
        else:
            new_instance = self.Models[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            splitted = arg.strip().split()
            if splitted[0] not in self.Models:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                id = splitted[1]
                key = "{}.{}".format(splitted[0], id)
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg not in self.Models:
            print("** class doesn't exist **")
        else:
            for key, value in models.storage.all().items():
                if arg == key.split(".")[0]:
                    print(value)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            splitted = arg.strip().split()
            if splitted[0] not in self.Models:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                id = splitted[1]
                key = "{}.{}".format(splitted[0], id)
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            splitted = arg.strip().split()
            if splitted[0] not in self.Models:
                print("** class doesn't exist **")
            elif len(splitted) < 2:
                print("** instance id missing **")
            else:
                id = splitted[1]
                key = "{}.{}".format(splitted[0], id)
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    if len(splitted) < 3:
                        print("** attribute name missing **")
                    elif len(splitted) < 4:
                        print("** value missing **")
                    else:
                        setattr(models.storage.all()[
                                key], splitted[2], splitted[3])
                        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
