#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    mem = {}
    num = 0
    for i, curr in enumerate(arr):
        idealEl = i + 1
        if curr == idealEl:
            continue

        if idealEl in mem:
            if mem[idealEl] == curr:
                num += 1
                del mem[idealEl]
                continue
        mem[curr] = idealEl

    # We can think the way we do swap as graph
    # Explaination that helps: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
    memKey = list(mem.keys())
    allVisited = set()

    for k in memKey:
        if k in allVisited:
            continue

        visited = set()
        nxt = k

        while nxt not in visited:
            visited.add(nxt)
            nxt = mem[nxt]

        num += (len(visited) - 1)
        allVisited = allVisited.union(visited)

    return num

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
