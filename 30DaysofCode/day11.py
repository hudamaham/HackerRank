#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
i=0 
j=0
l=list()
while(j+2<len(arr)):
    s=0
    i=0
    while( i+2<len(arr)):
        s=arr[j][i]+arr[j][i+1]+arr[j][i+2]+arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
        l.append(s)
        i=i+1
    j=j+1
print(max(l))
