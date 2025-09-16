#!/usr/bin/env python3
from sys import argv
""" scan_it.py """
def main():
    """ scan_it.py """
    if len(argv) == 3:
        num = (argv[2].split(' ')).count(argv[1])
        if num > 0:
            print(num)
        else:
            print("none")
    else:
        print("none")

main()
