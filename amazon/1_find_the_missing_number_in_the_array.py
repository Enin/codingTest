###
# You are given an array of positive numbers from 1 to n, such that all numbers
# from 1 to n are present except one number x. You have to find x. The input array is not sorted.
# Look at the below array and give it a try before checking the solution.
# 1
import random


def find_missing(input): # input is list
    total_sum = sum(input)

    n = len(input) + 1
    actual_sum = n * (n+1)/2
    return int(actual_sum - total_sum)

def test(n):
    missing_element = random.randint(1,n)
    v = []
    for i in range (1, n):
        if i != missing_element:
            v.append(i)

    actual_missing = find_missing(v)
    print("The missing number is {}, we find missing number as {}".format(missing_element, actual_missing))

def main():
    for n in range(1,10):
        test(100000)

main()
