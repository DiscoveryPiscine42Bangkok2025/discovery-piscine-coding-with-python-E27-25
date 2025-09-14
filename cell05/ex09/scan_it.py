#!/usr/bin/env python3
from sys import argv
""" scan_it.py """
def main():
    """ scan_it.py """
    if len(argv) == 3:
        print((argv[2].split(' ')).count(argv[1]))
    else:
        print('none')

main()
