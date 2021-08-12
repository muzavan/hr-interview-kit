#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangleArr(arr):
    if len(arr) == 0:
        return 0
    
    stack = [(arr[0], 0)]
    mx = arr[0]
    
    i = 1
    while i < len(arr):
        a = arr[i]
        t, _ = stack[-1]
        ci = i
        while a < t:
            t, ci = stack.pop()
            mx = max(mx, (i-ci)*t)
            if len(stack) == 0:
                break
            t, _ = stack[-1]
        
        stack.append((a, ci))
        i += 1
    
    ti = stack[-1][1]
    while stack:
        t, ci = stack.pop()
        mx = max(mx, (ti+1-ci) * t)
    
    return mx

def largestRectangle(h):
    return largestRectangleArr(h)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
