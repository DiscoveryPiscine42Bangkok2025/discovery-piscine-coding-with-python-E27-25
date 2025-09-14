#!/usr/bin/env python3
""" iszero.py """
def main():
    """ iszero.py """
    try:
        num = int(input())
        if num == 0:
            print('This number is equal to zero.')
        else:
            print('This number is different from zero.')
    except:
        print('It\'s str na ja')

main()
