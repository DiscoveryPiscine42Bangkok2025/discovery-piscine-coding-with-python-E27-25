#!/usr/bin/env python3
from sys import argv
""" downcase_it.py """
def main():
    """ downcase_it.py """
    if len(argv) == 2:
        print(argv[1].lower())
    else:
        print('none')

main()