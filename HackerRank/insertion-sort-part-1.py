#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    if n == 1:
        print(*arr)
        return
    val = arr[-1]
    arr = arr[:-1]
    for i in range(n-2,-1,-1):
        if arr[i] >= val:
            print(*arr[:i], arr[i], *arr[i:])
        else:
            print(*arr[:i+1], val, *arr[i+1:])
            return
    print(val, *arr[:])

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
