#!/usr/bin/env python3
""" multiplication_table.py """
def main():
    """ multiplication_table.py """
    try:
        num = int(input('Enter a number\n'))
        for i in range(13):
            print(f'{i} x {num} = {num*i}')
    except:
        print('STR Ya Sai')

main()
