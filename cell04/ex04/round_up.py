#!/usr/bin/env python3
from math import ceil
""" round_up.py """
def main():
    """ round_up.py """
    try:
        num = float(input('Give me a number: '))
        print(ceil((num)))
    except:
        print('STR is not avaiable')

main()
