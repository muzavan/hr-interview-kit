#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**10 + 7

# Complete the stepPerms function below.
def stepPerms(n):
    dp = {} # nth step -> number of possible way
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        poss = dp[i-3]
        poss %= MOD
        poss += dp[i-2]
        poss %= MOD
        poss += dp[i-1]
        poss %= MOD
        
            
        dp[i] = poss
    
    return dp[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
