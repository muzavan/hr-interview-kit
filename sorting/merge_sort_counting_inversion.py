#!/bin/python3

import math
import os
import random
import re
import sys

# st and en inclusive
def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    md = len(arr) // 2
    
    arr1, c1 = mergeSort(arr[:md])
    arr2, c2 = mergeSort(arr[md:])
    
    cnt = c1 + c2
    
    N1 = len(arr1)
    N2 = len(arr2)
    i1, i2 = 0, 0
    
    while i1 < N1 and i2 < N2:
        if arr1[i1] <= arr2[i2]:
            arr[i1 + i2] = arr1[i1]
            i1 += 1
        else:
            cnt += len(arr1) - i1
            arr[i1 + i2] = arr2[i2]
            i2 += 1
    
    if i1 < N1:
        arr = arr[:i1+i2] + arr1[i1:]
    if i2 < N2:
        arr = arr[:i1+i2] + arr2[i2:]
        
    return arr, cnt
    
# Complete the countInversions function below.
def countInversions(arr):
    # Just to make sure we can pass the value as reference
    _, cnt = mergeSort(arr)
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
