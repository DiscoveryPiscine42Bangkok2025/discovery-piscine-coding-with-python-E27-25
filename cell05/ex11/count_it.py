#!/usr/bin/env python3
from sys import argv
""" count_it.py """
def main():
    """ count_it.py """
    if len(argv) >= 2:
        print('parameters:', len(argv)-1)
        for txt in argv[1:]:
            print(f'{txt}: {len(txt)}')
    else:
        print('none')

main()