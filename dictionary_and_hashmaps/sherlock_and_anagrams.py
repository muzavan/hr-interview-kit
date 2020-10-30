#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # naive idea
    # iterate through all possible substring
    # see if it has the same collection of chars
    cnt = 0

    for numChar in range(1, len(s)):
        mem = {}
        for i in range(0, len(s) - numChar + 1):
            currStr = ''.join(sorted(s[i:i+numChar]))

            if currStr not in mem:
                mem[currStr] = 0

            cnt += mem[currStr]
            mem[currStr] += 1

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
