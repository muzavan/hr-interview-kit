#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def glassShape(x, y):
    moveSet = [
        (0, 0),(1, 0), (2, 0),
               (1, 1),
        (0, 2),(1, 2), (2, 2),
    ]

    return [(x+xi, y+yi) for xi, yi in moveSet]


def hourglassSum(arr):
    alls = []

    for x in range(0, 4):
        for y in range(0, 4):
            glass = sum([arr[b][a] for a, b in glassShape(x, y)])
            alls.append(glass)

    return max(alls)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
