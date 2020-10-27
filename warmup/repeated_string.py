#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    slen = len(s)
    aidxs = [i+1 for i, c in enumerate(s) if c == 'a']

    total = 0
    multiplier = n // slen
    total = multiplier * len(aidxs)

    mod = n % slen
    for idx in aidxs:
        if idx > mod:
            break
        total += 1

    return total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
