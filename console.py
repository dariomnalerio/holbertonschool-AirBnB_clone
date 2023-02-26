#!/usr/bin/python3
""" AirBnb Console """
import cmd
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'City': City, 'Amenity': Amenity,
               'Place': Place, 'Review': Review}

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Ctrl-D"""
        return True

    def emptyline(self):
        """
        Method to pass when emptyline entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the class BaseModel
        """

        if (arg):
            splited_arguments = arg.split()
            if len(splited_arguments) == 1:
                if arg in self.classes.keys():
                    new_instance = self.classes[arg]()
                    new_instance.save()
                    print(new_instance.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Print the string representation of a Instance with their id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        argument = arg.split()
        if not argument[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                saved = storage.all()
                print(saved[key])
            else:
                print('** no instance found **')
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return

        argument = arg.split()
        if not argument[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(argument) > 1:
            key = argument[0] + '.' + argument[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
            return
        if not arg.split()[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if arg in self.classes.keys():
            for a in storage.all():
                print(str(a))

    def do_update(self, arg):
        """
        Updates an instance based on the class name
         and id by adding or updating attribute.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        argument = arg.split()
        if not argument[0] in self.classes.keys():
            print("** class doesn't exist **")
            return

        if len(argument) == 1:
            print("** instance id missing **")
            return
        key = argument[0] + '.' + argument[1]
        if len(argument) > 2:
            if len(argument) == 3:
                print("** value missing **")
            else:
                if key in storage.all():
                    setattr(storage.all()[key], argument[2], argument[3][:])
                    storage.all()[key].save()
                else:
                    print('** no instance found **')
        else:
            print("** attribute name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
