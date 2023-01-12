#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 18:17:23 2018

@author: gabriel
"""

def get_data(bTuple):
    nums = ()
    words = ()
    for t in bTuple:
        nums = nums + (t[0],)
        if t[1] not in  words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
print(get_data(bTuple))   
    
(small, large, words) = get_data(bTuple)