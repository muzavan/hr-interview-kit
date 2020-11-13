#!/bin/python3

import math
import os
import random
import re
import sys

# I am struggling to find which list comprehension is the fastest
# It's returning TLE for some case if I use other approach :(
def commonChild(s1, s2):
    N = len(s1)
    prev = [0] * (N + 1)
    curr = prev[:]
    for ss1 in s1:
        for j, ss2 in enumerate(s2):
            bst = 0
            if ss1 == ss2:
                bst = prev[j] + 1
            else:
                bst = max(curr[j], prev[j+1])
                
            curr[j+1] = bst
        
        prev, curr = curr, prev
            
                
    return prev[-1]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
