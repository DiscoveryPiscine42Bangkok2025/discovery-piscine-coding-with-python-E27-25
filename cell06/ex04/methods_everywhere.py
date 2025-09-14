#!/usr/bin/env python3
from sys import argv
""" methods_everywhere.py """
class Main1():
    def __init__(txt):
        """ shrink """
        indx = slice(8)
        print(txt[indx])

class Main2():
    def __init__(txt):
        """ enlarge """
        num = max(8-len(txt), 0)
        print(txt + 'Z'*num)

shrink = Main1.__init__
enlarge = Main2.__init__

if len(argv) > 1:
    for txt in argv[1:]:
        if len(txt) >= 8:
            shrink(txt)
        else:
            enlarge(txt)
else:
    print('none')
