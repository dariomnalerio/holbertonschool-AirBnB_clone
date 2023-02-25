#!/usr/bin/python3
""" AirBnb Console """
import cmd
from models.base_model import BaseModel
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    
    prompt = '(hbnb) '
    classes = {'BaseModel' : BaseModel}

    def do_quit(self,arg):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """Ctrl-D"""
        return True

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """Creates a new instance of the class BaseModel"""
        
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
        """Print the string representation of a Intance with their id"""
        if len(arg) == 0:
            print("** class name missing **")
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
        "Delete a instance of the class BaseMode"
        if len(arg) == 0:
            print("** class name missing **")
            return
        
        arguments = arg.split()
        if not arguments[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(arguments) > 1:
            key = arguments[0] + '.' + arguments[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        if not arg.split()[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if arg in self.classes.keys():
            for a in storage.all():
                print(str(a))

        

if __name__ == '__main__':
    HBNBCommand().cmdloop()