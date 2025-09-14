#!/usr/bin/env python3
from sys import argv
""" aff_rev_params.py """
def main():
    """ aff_rev_params.py """
    if len(argv) > 2:
        print(*argv[1:][::-1], sep='\n')
    else:
        print('none')

main()
