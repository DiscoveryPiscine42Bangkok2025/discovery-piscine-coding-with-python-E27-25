#!/usr/bin/env python3
from sys import argv
""" scope_that.py """
class Main():
    def __init__(num):
        """ add_one """
        return num+1

add_one = Main.__init__

if len(argv) == 1:
    numed = 5
    result = add_one(numed)
    print(numed)
    print(result)
else:
    print('none')
