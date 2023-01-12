#!/usr/bin/env python3


def linecount(t):
        count=0
        for line in open(t):
                count+=1
        return count

if __name__ == '__main__':
 print(linecount('wc.py'))

