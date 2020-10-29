#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arrs = [0] * n

    for q in queries:
        st, en, val = q[0], q[1], q[2]

        # Using prefix sum technique
        st -= 1
        arrs[st] += val

        if en < len(arrs):
            arrs[en] -= val

    mx = 0
    sm = 0
    for a in arrs:
        sm = sm + a
        mx = max(mx, sm)
    
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
