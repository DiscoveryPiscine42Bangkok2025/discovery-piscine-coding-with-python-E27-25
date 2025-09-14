#!/usr/bin/env python3
""" float.py """
def main():
    """ float.py """
    try:
        num = input('Give me a number: ')
        check = num
        num = float(num)
        num = check
        
        num = num.split('.')
        if len(num) == 1 or int(num[1] ) == 0:
            print('This number is an integer.')
        else:
            print('This number is a decimal.')
    except:
        print('It\'s STR NAJAA')

main()
