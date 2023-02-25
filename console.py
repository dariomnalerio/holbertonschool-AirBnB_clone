#!/usr/bin/python3
""" AirBnb Console """
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self,arg):
        """Quit command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """Ctrl-D"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()