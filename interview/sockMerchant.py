#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    setN=set()
    for e in ar:
        n=ar.count(e)
        t=(e,n)
        setN.add(t)
    s=0
   
    for e in setN:
        s=s+(e[1]-e[1]%2)/2
    return int(s)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
