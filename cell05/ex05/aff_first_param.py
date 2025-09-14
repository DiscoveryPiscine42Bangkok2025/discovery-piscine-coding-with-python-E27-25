#!/usr/bin/env python3
from sys import argv
""" aff_first_param.py """
def main():
    """ aff_first_param.py """
    if len(argv) >= 2:
        print(argv[1])
    else:
        print('none')

main()
