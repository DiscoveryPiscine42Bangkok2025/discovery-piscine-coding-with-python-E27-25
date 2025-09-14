#!/usr/bin/env python3
""" password.py """
def main():
    """ password.py """
    password = "Python is awesome"
    txt = input()
    print('ACCESS GRANTED') if txt == password else print('ACCESS DENIED')

main()
