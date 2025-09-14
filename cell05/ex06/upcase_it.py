#!/usr/bin/env python3
from sys import argv
""" upcase_it.py """
def main():
    """ upcase_it.py """
    if len(argv) == 2:
        print(argv[1].upper())
    else:
        print('none')

main()
