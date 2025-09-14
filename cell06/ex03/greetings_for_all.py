#!/usr/bin/env python3
from sys import argv
""" greetings_for_all.py """
class Main():
    def __init__(*name):
        """ greetings_for_all.py  """
        if len(argv) == 1:
            name = [i for i in name]
            if name == []:
                print(f"Hello, noble stranger.")
            elif isinstance(name[0], int) == True:
                print("Error! It was not a name.")
            else:
                print(f"Hello, {str(name[0])}.")
        else:
            print('none')

greetings = Main.__init__

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
