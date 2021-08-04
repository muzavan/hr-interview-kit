#!/bin/python3

import math
import os
import random
import re
import sys

# Learn about Disjoint Set!
# This helps: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

class FriendGroup:
    def __init__(self, num):
        self.parent = None
        self.num = num
        self.size = 1
        
    def root(self):
        curr = self
        while curr.parent is not None:
            curr, curr.parent = curr.parent, curr.parent.parent
        return curr
    
    def merge(self, fg):
        s_root = self.root()
        f_root = fg.root()
        
        if s_root.num == f_root.num:
            return s_root.size
        
        if s_root.size < f_root.size:
            return f_root.merge(s_root)
        
        s_root.size += f_root.size
        f_root.parent = s_root
        return s_root.size
        
    def __len__(self):
        root = self.root()
        return root.size

# Complete the maxCircle function below.
def maxCircle(queries):
    fg_map = {}
    
    result = []
    mx_friend = 0
    for [f1, f2] in queries:
        if f1 not in fg_map:
            fg_map[f1] = FriendGroup(f1)
        if f2 not in fg_map:
            fg_map[f2] = FriendGroup(f2)
        
        fg1 = fg_map[f1]
        fg2 = fg_map[f2]
        new_size = fg1.merge(fg2)
        mx_friend = max(mx_friend, new_size)
        result.append(mx_friend)
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
