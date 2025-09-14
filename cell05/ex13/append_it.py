#!/usr/bin/env python3
from sys import argv
""" append_it.py """
def main():
    """ append_it.py """
    if len(argv) >= 2:
        for txt in argv[1:]:
            if txt.endswith('ism') == False:
                txt = txt.rstrip('e') + 'ism'
                print(txt)
    else:
        print('none')

main()
