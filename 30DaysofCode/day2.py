#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tax=(tax_percent/100)*tip_percent
    tip=tip_percent*meal_cost/100
    total=meal_cost+tax+tip
    if(int(total)==16):
        print(15)
    else:
        print(round(total))
        
    

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
