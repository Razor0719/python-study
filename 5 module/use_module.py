#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
'test module'
__author__='razor0719'

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private1():
    return 'private1'
def __private2():
    return 'private2'

if __name__=='__main__':
    test()
    print(_private1())
    print(__private2())