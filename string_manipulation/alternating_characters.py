#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    mem = {
        'A': 'B',
        'B': 'A',
    }
    
    cnt = 0
    prev = s[0]
    for ss in s[1:]:
        needed = mem[prev]        
        if ss != needed:
            cnt += 1
        else:
            prev = ss
    
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
