#!/usr/bin/env python3
""" isneg.py """
def main():
    """ isneg.py """
    try:
        num = float(input())
        result = 'positive and negative'

        if num < 0:
            result = 'negative'
        elif num > 0:
            result = 'positive'

        print(f'The result is {result}.')

    except:
        print('It\'s str naja.')

main()
