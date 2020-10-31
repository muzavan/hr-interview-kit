#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    cnt = 0

    # mem2: map[num1]: cnt -> count of num1
    mem1 = {}
    # mem2: map[(num1, num2)]: cnt -> count of pair of (num1, num2), assuming num2//num1 == r
    mem2 = {}
    for a in arr:
        num2 = a / r
        num1 = num2 / r

        if (num1, num2) in mem2:
            cnt += mem2[(num1, num2)]

        if num2 in mem1:
            if (num2, a) not in mem2:
                mem2[(num2, a)] = 0

            mem2[(num2, a)] += mem1[num2]

        if a not in mem1:
            mem1[a] = 0

        mem1[a] += 1
    
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
