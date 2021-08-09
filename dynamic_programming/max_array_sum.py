#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    mxs = [] #(mx_sum, used)
    for i, a in enumerate(arr):
        prev_mx = 0
        used = False 
        if len(mxs) > 0:
            prev_mx, used = mxs[-1]
            
        if a <= 0:
            mxs.append((prev_mx, False))
            continue
        
        # a > 0
        p1, u1 = 0, False
        if len(mxs) > 0:
            p1, u1 = mxs[-1]
        
        if not u1:
            mxs.append((prev_mx + a, True))
            continue
        
        p2, u2 = 0, False
        if len(mxs) > 1:
            p2, u2 = mxs[-2]
            
        p = p2 + a
        if p1 >= p:
            mxs.append((p1, False))
        else:
            mxs.append((p, True))
            
    return max(mxs)[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
