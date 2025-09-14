#!/usr/bin/env python3
""" to25.py """
def main():
    """ to25.py """
    try:
        num = int(input('Enter a number less than 25\n'))
    
        if num > 25:
            print('Error')
        else:
            while num <= 25:
                print(f'Inside the loop, my variable is {num}')
                num += 1
    except:
        print('Not support STR na')

main()
