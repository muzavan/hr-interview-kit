#!/bin/python3

import math
import os
import random
import re
import sys

QUERY_INSERT = 1
QUERY_DELETE = 2
QUERY_COUNT = 3

# Complete the freqQuery function below.
def freqQuery(queries):
    valueCountMap = {}
    countValueMap = {}

    res = []
    for query in queries:
        query_type, query_param = query[0], query[1]

        if query_type == QUERY_INSERT:
            if query_param not in valueCountMap:
                valueCountMap[query_param] = 0

            oldCount = valueCountMap[query_param]
            newCount = oldCount + 1
            valueCountMap[query_param] = newCount

            if oldCount in countValueMap:
                countValueMap[oldCount].remove(query_param)

            if newCount not in countValueMap:
                countValueMap[newCount] = set()

            countValueMap[newCount].add(query_param)
            continue

        if query_type == QUERY_DELETE:
            if query_param not in valueCountMap or valueCountMap[query_param] == 0:
                continue

            oldCount = valueCountMap[query_param]
            newCount = oldCount - 1
            valueCountMap[query_param] = newCount

            if newCount != 0:
                if newCount not in countValueMap:
                    countValueMap[newCount] = set()

                countValueMap[newCount].add(query_param)

            countValueMap[oldCount].remove(query_param)

            continue

        if query_type == QUERY_COUNT:
            if query_param not in countValueMap or len(countValueMap[query_param]) == 0:
                res.append(0)
                continue

            res.append(1)
            continue
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
