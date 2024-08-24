'''
Link to the Question: https://www.hackerrank.com/challenges/apple-and-orange/problem

walk-through:
7 11 --> s (starting pos of house) t (ending pos of house)
5 15 --> a (apple tree position) b (orange tree position) 
3 2 --> m (no. of apples) n (no. of oranges)
-2 2 1 --> m[i] (position of the fallen apple's distance from tree)
-5 6 --> n [i] (position of the fallen oranges's distance from tree)


'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_count = 0
    b_count = 0
    for i in range(len(apples)):
        a_updated = a+apples[i]
        if(a_updated in range(s,t+1)):
            a_count+=1
    for i in range(len(oranges)):
        b_updated = b+oranges[i]
        if(b_updated in range(s,t+1)):
            b_count+=1
    print (a_count)
    print (b_count)
        
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)





