#!/usr/bin/env python3
from sys import argv
""" downcase_all.py """
class Main():
    def __init__(txt):
        """ downcase_all.py """
        if len(argv) >= 2:
            lst = [i.lower() for i in txt]
            print(*lst, sep='\n')
        else:
            print('none')

downcase_it = Main.__init__

downcase_it(argv[1:])
