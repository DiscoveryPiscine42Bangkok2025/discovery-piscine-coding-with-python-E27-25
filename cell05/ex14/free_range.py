#!/usr/bin/env python3
from sys import argv
""" free_range.py """
def main():
    """ free_range.py """
    if len(argv) == 3:
        if int(argv[1]) > int(argv[2]):
            print(list(range(int(argv[2]), int(argv[1])+1))[::-1])
        else:
            print(list(range(int(argv[1]), int(argv[2])+1)))
    else:
        print('none')

main()
