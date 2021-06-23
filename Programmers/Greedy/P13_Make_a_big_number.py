#  큰 수 만들기
#
# 문제 설명
#
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
#
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
#  number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
# 제한 조건
#
#     number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#     k는 1 이상 number의 자릿수 미만인 자연수입니다.

# dfs를 사용

from itertools import permutations
from collections import deque

max_ans = 0


def solution(number, k):
    global max_ans
    num_list = list(number)
    answer = ''.join(num_list)

    if k == 0:
        max_ans = max(max_ans, answer)
        return answer



        number = solution(number, k)


    return answer


def dfs(number, k, answer):
    return 0


i_number, k = "1231234", 3


# print(solution(i_number, k))
