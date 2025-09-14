#!/usr/bin/env python3
from sys import argv
""" parameter_matching.py """
def main():
    """ parameter_matching.py """
    if len(argv) == 2:
        txt = input('What was the parameter? ')
        print('Good job!') if txt == argv[1] else print('Nope, sorry...')
    else:
        print('none')

main()
