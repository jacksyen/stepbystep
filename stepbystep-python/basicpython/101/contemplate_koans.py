#!/usr/bin/env python
# -*- coding: utg-8 -*-

import sys

if __name__=='__main__':
    if sys.version_info>=(3,0):
        print("\nThis is the python 2 version ")
    else:
        if sys.version_info<(2,7):
            print("python version")


        f