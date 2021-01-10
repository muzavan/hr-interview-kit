#!/bin/python3

import math
import os
import random
import re
import sys

dMap = {}
# Complete the superDigit function below.

# Just so happen, I just watched this video: https://www.youtube.com/watch?v=QNPq4VKD7ic
def superDigit(n, k):
    global dMap
    
    if n == 0:
        return 0
    
    if (n, k) in dMap:
        return dMap[(n, k)]
    
    digit = n % 9
    if digit == 0:
        digit = 9
    
    if k == 1:
        dMap[(n, k)] = digit
        return digit
    
    if k%9 == 0 or digit%9 == 0:
        dMap[(n, k)] = digit
        return digit
    
    digit = superDigit(digit*k,1)
    dMap[(n, k)] = digit
    return digit
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
