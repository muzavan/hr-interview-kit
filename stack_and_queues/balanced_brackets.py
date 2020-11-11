#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    
    for ss in s:
        if ss == '}':
            if len(stack) == 0 or stack[-1] != '{':
                return "NO"
            stack.pop(-1)
            continue
        
        if ss == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return "NO"
            stack.pop(-1)
            continue
        if ss == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return "NO"
            stack.pop(-1)
            continue
        stack.append(ss)
    
    if stack:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
