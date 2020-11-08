#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    da = {}
    db = {}
    
    for aa in a:
        if aa not in da:
            da[aa] = 0
        da[aa] += 1
        
    for bb in b:
        if bb not in db:
            db[bb] = 0
            
        db[bb] += 1
        
    cnt = 0
    for ka, va in da.items():
        if ka not in db:
            db[ka] = 0
        
        cnt += max(va, db[ka]) - min(va, db[ka])
        db[ka] = va
        
    for kb, vb in db.items():
        if kb not in da:
            da[kb] = 0
        
        cnt += max(vb, da[kb]) - min(vb, da[kb])
        da[kb] = vb
    
    return cnt
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
