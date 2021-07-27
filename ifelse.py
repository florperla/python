#!/bin/python3

import math
import os
import random
import re
import sys

""" If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
"""

if __name__ == '__main__':
    n = int(input().strip())

    if 2<n<5 and int(n%2 == 0):
        print ("Not Weird")
    elif 6<n<20 and int(n%2 == 0):
        print ("Weird")
    elif n>20 and int(n%2 == 0):
        print ("Not Weird")
    else:
        print("Weird")
