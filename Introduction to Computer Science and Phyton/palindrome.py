#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:01:09 2018

@author: gabriel
"""

def palindrome(s):
    def tochars(s):
        s= s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def ispal(s):
        if len(s) <=1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])
    return ispal(tochars(s))

print (palindrome('Arara'))