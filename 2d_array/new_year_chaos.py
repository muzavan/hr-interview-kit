#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total = 0
    n = len(q)

    bribed = set()
    for i in range(n-1, -1, -1):
        idealPos = i + 1
        curr = q[i]

        mv = curr - idealPos
        if mv > 2:
            print("Too chaotic")
            return

        j = max(curr - 2, 0)

        while j < i:
            if q[j] > curr:
                total += 1
            j += 1 

    print(total)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
