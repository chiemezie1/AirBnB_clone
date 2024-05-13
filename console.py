#!/usr/bin/python3
"""AirBnB_clone Console Module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter for AirBnB Clone"""
    prompt = "(hbnb) "
    cmd = cmd.Cmd()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
