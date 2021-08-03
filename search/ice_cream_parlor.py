#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    prev_costs = {} # cost -> actIndex
    for idx, c in enumerate(cost):
        act_idx = idx + 1 # using 1-index
        needed = money - c
        if needed in prev_costs:
            print(prev_costs[needed], act_idx)
            return   
        prev_costs[c] = act_idx

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
