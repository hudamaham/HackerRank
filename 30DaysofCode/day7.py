#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    i=len(arr)-1
    l=list()
    while(i>=0):
        l.append(arr[i])
        i=i-1
    s=''
    for e in l :
        s=s+str(e)+' '
    s.strip()
    print(s)
