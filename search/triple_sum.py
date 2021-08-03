#!/bin/python3

import math
import os
import random
import re
import sys

def findLast(el, ls, start, en):
    last = ls[en]
    if last <= el:
        return en
    mid = (start + en) // 2
    curr = ls[mid]
    if curr > el:
        if en <= start:
            return -1
        return findLast(el, ls, start, mid-1)
    
    if curr == el or mid == en or ls[mid+1] > el:
        return mid
    return findLast(el, ls, mid+1, en)
    
    

# Complete the triplets function below.
def triplets(a, b, c):
    a = set(a)
    b = set(b)
    c = set(c)
    
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)
    
    # Populate the data
    total = 0
    for bb in b:
        ai = findLast(bb, a, 0, len(a)-1)
        ci = findLast(bb, c, 0, len(c)-1)
        
        total += (ai + 1) * (ci + 1)
        
        # print("A", ai, bb)
        # print("C", ci, bb)
    
    return total
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
