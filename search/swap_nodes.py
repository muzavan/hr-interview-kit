#!/bin/python3

import os
import sys

from collections import defaultdict

def get_inorder(indexes):
    if len(indexes) == 0:
        return []
    
    root = 1
    stack = []
    res = []
    while stack or root != -1:
        if root != -1:
            stack.append(root)
            a, b = indexes[root-1]
            root = a
        else:
            s = stack.pop(-1)
            res.append(s)
            a, b = indexes[s - 1]
            root = b            
    
    return res
    
def get_level_map(indexes):
    level_map = defaultdict(list)
    if len(indexes) == 0:
        return level_map
    
    root = (1, 1)
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            a, b = indexes[root[0]-1]
            if a != -1:
                root = (a, root[1] + 1)
            else:
                root = None
        else:
            s = stack.pop(-1)
            level_map[s[1]].append(s[0])
            a, b = indexes[s[0] - 1]
            if b != -1:
                root = (b, s[1] + 1)
            else:
                root = None
    
    return level_map
#
# Complete the swapNodes function below.
#

def swapNodes(indexes, queries):
    if len(indexes) == 0:
        return []
    lm = get_level_map(indexes)
    # from pprint import pprint
    # pprint(lm)
    # return
    res = []
    for q in queries:
        for n in range(1, 1025):
            h = n * q
            if h not in lm:
                break
            
            for idx in lm[h]:
                a, b = indexes[idx-1]
                indexes[idx-1] = (b, a)
                
        res.append(get_inorder(indexes))
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
