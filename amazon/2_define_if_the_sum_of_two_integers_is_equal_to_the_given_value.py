###
# Given an array of integers and a value,
# determine if there are any two integers in the array whose sum is equal to the given value.
# Return true if the sum exists and return false if it does not.
# Consider this array and the target sums:
# 해싱 문제
import random


def find_sum_of_two(list, val): # list 는 입력된 리스트. val은 타겟 sum 값
    find_values = set() # set 해쉬를 사용해서 in 조건을 사용할 수 있음.
    for i in list:
        if val - i in find_values:
            return True

        find_values.add(i)

    return False


def test(n):
    target_sum = random.sample(range(1,n*3), 5)
    given_list = random.sample(range(1,n), n-1)

    for i in target_sum:
        check_result = find_sum_of_two(given_list, i)
        print("Target sum is {}, and given list is {}, find sum of two result is {}".format(i, given_list, check_result))

def main():
    test(9)

main()