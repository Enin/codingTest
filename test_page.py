#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'substringCalculator' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#
from itertools import permutations

def substringCalculator(s):
    # Write your code here

    subset = set()
    s_len = len(s)

    for i in range(s_len):  # i: 시작점
        for j in range(s_len + 1, i, -1):  # j: 끝점
            if s[i:j] not in subset:
                subset.add(s[i:j])
    for idx, subs in enumerate(subset):
        print(f'{idx} {subs}')


    return len(subset)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'kincenvizh'

    result = substringCalculator(s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
