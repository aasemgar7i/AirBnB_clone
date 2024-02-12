#!/usr/bin/python3
"""HBNB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class representing the command interpreter.

    Attributes:
        prompt (str): Custom prompt for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn’t execute anything.
        """
        pass

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit the program")

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit the program")

    def default(self, line):
        """
        Default method called when the entered command is not recognized.
        """
        print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
