#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    poss = [(0, 0)]

    mn = len(c) + 1 # arbitary number as initial mn
    while poss:
        idx, jump = poss.pop()
        if idx >= len(c) or c[idx] == 1:
            continue

        if idx == len(c) - 1:
            mn = min(mn, jump)
            continue

        poss.append((idx+1, jump+1))
        poss.append((idx+2, jump+1))

    return mn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
