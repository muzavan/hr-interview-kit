#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    # since it's guaranteed that
    # the element is unique
    visited = set()
    cnt = 0
    for a in arr:
        needed1 = a - k
        needed2 = a + k
        if needed1 in visited:
            cnt += 1
        if needed2 in visited:
            cnt += 1
        visited.add(a)
        
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
