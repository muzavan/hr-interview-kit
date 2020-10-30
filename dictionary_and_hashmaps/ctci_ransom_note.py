#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mem = {}
    for m in magazine:
        if m not in mem:
            mem[m] = 0
        mem[m] += 1

    for n in note:
        if n in mem and mem[n] > 0:
            mem[n] -= 1
            continue
        print("No")
        return

    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
