#!/usr/bin/env python3
import sys
""" advanced_mult.py """
def main():
    """ advanced_mult.py """
    if len(sys.argv) >= 2:
        return print('none')

    i = 0
    while i <= 10:
        x = 0
        print(f'Table de {i}:', end='')
        while x <= 10:
            print(f' {i*x}', end='')
            x += 1
        print()
        i += 1

main()
