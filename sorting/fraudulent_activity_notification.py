#!/bin/python3

import math
import os
import random
import re
import sys

def replaceElement(arr, kicked, new):
    # Remove
    st, en = 0, len(arr) - 1
    
    # Kicked guaranted to exist in arr
    while en >= st:
        md = (en + st) // 2
        
        a = arr[md]
        if a == kicked:
            arr.pop(md)
            break
        
        if kicked < a:
            en = md - 1
            continue
        
        st = md + 1
        
    st, en = 0, len(arr) - 1
    
    # Insert new element
    while en > st:
        md = (en + st) // 2
        
        a = arr[md]
        if a < new:
            st = md + 1
            continue
        
        if a == new:
            arr.insert(md, new)
            return
        
        en = md - 1
    
    # st == en
    if arr[en] == new:
        arr.insert(en, new)
        return
        
    if arr[en] > new:
        for i in range(en-1, -1, -1):
            a = arr[i]
            if a < new:
                arr.insert(i+1, new)
                return
                
        arr.insert(0, new)
        return
    
    for i in range(en+1, len(arr)):
        a = arr[i]
        if a >= new:
            arr.insert(i, new)
            return
            
    arr.append(new)
            
            
        
        

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # Idea, maintain the d prev expenditure
    # Using binary search to insert element
    
    cnt = 0
    
    prevs = sorted(expenditure[:d])
    
    for i in range(d, len(expenditure)):
        curr = expenditure[i]
        
        md = d // 2
        med = prevs[md]
        
        if d%2 == 0:
            med += prevs[md-1]
            med /= 2
            
        if curr >= (2 * med):
            cnt += 1
            
        kicked = expenditure[i-d]
        
        replaceElement(prevs, kicked, curr)

    return cnt
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
