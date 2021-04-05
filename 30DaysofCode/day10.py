#!/bin/python3

import math
import os
import random
import re
import sys

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 

if __name__ == '__main__':
    n = int(input())
    s=decimalToBinary(n)
    l=list()
    k=0
    for c in s :
        if(c=='1'):
            k=k+1
        else :
            l.append(k)
            k=0
        l.append(k)
    print(max(l))
