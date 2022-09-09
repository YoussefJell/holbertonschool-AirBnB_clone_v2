#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime

globalClasses = ('BaseModel', 'User', 'State',
                 'Amenity', 'City', 'Place', 'Review')


class HBNBCommand(cmd.Cmd):
    """console that contains the entry point of the command interpreter"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        'Exits the HBNB console'
        return True

    def do_quit(self, arg):
        'Exits the HBNB console'
        return True

    def emptyline(self):
        """What happens if you put an empty line (Enter)"""
        pass

    def do_create(self, line):
        'Creates a new instance of BaseModel.'
        args = line.split(' ')
        if len(args[0]) == 0:
            print("** class name missing **")
            return
        elif len(args[0]) >= 1 and args[0] not in globalClasses:
            print("** class doesn't exist **")
            return

        myobj = eval(args[0])()
        if len(args) > 1:
            for kwords in args[1:]:
                my_map = kwords.split("=")

                if hasattr(myobj, my_map[0]):
                    setattr(myobj, my_map[0], eval(
                        my_map[1].replace("_", " ")))
        myobj.save()
        print(myobj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based \
 on the class name and id"""
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return

        elif len(args) >= 1 and args[0] not in globalClasses:
            print("** class doesn't exist **")
            return

        elif len(args) == 1 and args[0] in globalClasses:
            print("** instance id missing **")
            return

        elif len(args) == 2:

            storage.reload()
            myobjects = storage.all()

            if myobjects.get(f'{args[0]}.{args[1]}', 0):
                print(myobjects[f'{args[0]}.{args[1]}'])

            else:
                print("** no instance found **")

    def do_destroy(self, line):
        'Deletes an instance based on the class name and id'
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return

        elif len(args) >= 1 and args[0] not in globalClasses:
            print("** class doesn't exist **")
            return

        elif len(args) == 1 and args[0] in globalClasses:
            print("** instance id missing **")
            return

        elif len(args) == 2:

            storage.reload()
            myobjects = storage.all()

            if myobjects.get(f'{args[0]}.{args[1]}', 0):
                del myobjects[f'{args[0]}.{args[1]}']
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of\
 all instances based or not on the class name. """
        args = line.split(' ')

        if len(args[0]) == 0 or args[0] in globalClasses:
            storage.reload()
            if args[0] in globalClasses:
                myobjects = storage.all(args[0])
            else:
                myobjects = storage.all()
            list_obj = []
            for value in myobjects.values():
                list_obj.append(str(value))
            print(list_obj)

        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        'Updates an instance based on the class name and id'
        args = line.split(' ')

        if len(args[0]) == 0:
            print("** class name missing **")
            return
        elif len(args) >= 1 and args[0] not in globalClasses:
            print("** class doesn't exist **")
            return
        elif len(args) == 1 and args[0] in globalClasses:
            print("** instance id missing **")
            return

        storage.reload()
        myobjects = storage.all()

        if myobjects.get(f'{args[0]}.{args[1]}', 0):
            if len(args) == 2:
                print("** attribute name missing **")
                return

            elif len(args) == 3:
                print("** value missing **")
                return
            if args[3].isdigit():
                value = int(args[3])
            else:
                try:
                    value = float(args[3])
                except (ValueError, NameError):

                    if args[3][0] == '"' and args[3][-1] == '"':
                        value = args[3][1:len(args[3]) - 1]

                    elif len(args) == 5 and args[3][0] == '"'\
                            and args[4] == '"':
                        value = args[3][1:len(args[3])] + ' '

                    elif len(args) == 5 and args[3][0] == '"'\
                            and args[4][-1] == '"':
                        value = args[3][1:len(args[3])] + ' '\
                            + args[4][0:len(args[4]) - 1]

                    else:
                        value = args[3]

            setattr(myobjects[f'{args[0]}.{args[1]}'], args[2], value)
            setattr(myobjects[f'{args[0]}.{args[1]}'],
                    'updated_at', datetime.now())
            myobjects[f'{args[0]}.{args[1]}'].save()

        else:
            print("** no instance found **")
            return

    def clean_args(self, my_list):
        """remove unecessary chars"""
        my_class = my_list[0]
        rest_of_args = my_list[1][my_list[1].find('(')+1:my_list[1].find(')')]
        if len(rest_of_args) > 0:
            args = rest_of_args.replace(',', '')
            args = args.replace('"', '')

            return my_class + ' ' + args
        else:
            return my_class

    def default(self, line):
        """Method called on an input line when the\
                command prefix is not recognized"""
        args = line.split('.')
        if len(args) >= 2 and args[1]:
            if args[1][:4] == "show":
                self.do_show(self.clean_args(args))

            elif args[1][:7] == "destroy":
                self.do_destroy(self.clean_args(args))

            elif args[1] == "all()":
                self.do_all(args[0])

            elif args[1] == "count()":
                print(storage.count(args[0]))

            elif args[1][:6] == "update":
                self.do_update(self.clean_args(args))
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
