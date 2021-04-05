#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    m=s
    f=list()
    k=0
    e=0
    while e < len(m):
        if(m[k]==' ')or e==0:
            f.append(m[e].upper())
        else:
            f.append(m[e])

        k=e
        e=e+1
    finalS = ''.join(f)
    return finalS
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
