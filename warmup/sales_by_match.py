#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    mem = {}

    for a in ar:
        if a not in mem:
            mem[a] = 0
        mem[a] += 1

    cnt = 0
    for k, v in mem.items():
        cnt += (v // 2)

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
