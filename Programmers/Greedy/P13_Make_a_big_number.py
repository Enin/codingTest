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


candis = []


def solution_bad(number, k):    # 문자열, 뺄 숫자 갯수
    # 문자열을 숫자 리스트로 변경.
    list_number = list(map(int, number))
    dfs(list_number, 0, k)

    answer = str(max(candis))

    return answer


def dfs(list_n, now, k): # 숫자 리스트, 반복할 횟수.
    if now == k:
        join_n = int(''.join(map(str, list_n)))
        candis.append(join_n)

    else:
        len_n = len(list_n)
        for i in range(len_n):
            pop_one = list_n.pop(i) # i번째 리스트 값을 꺼냄
            dfs(list_n, now + 1, k)
            list_n.insert(i, pop_one)   # 꺼냈던 리스트 값을 다시 넣어줌.

## dfs 로 풀면 시간 너무 오래걸림. 다시 할것.
# 주의점 9가 있을 경우 해당 idx에서 시작하는 최적화.
# 리스트.index(값)을 사용하여 원하는 값이 있는 idx를 리턴받음. 없을 경우 에러가 발생됨.
# if v in l : l.index(v) 를 사용하여 값이 있는지 확인한 뒤 찾는다.
# 문자열을 건드리지 않은채 index 만 사용하여 접근하는 것이 가장 빠를 수 있음.

def solution(number, k):    # 문자열, 뺄 숫자 갯수
    answer = ''
    f_idx = 0
    len_number = len(number)

    list_number = list(map(int, number))

    for i in range(k):



    for j in range(k):

        for i in range(9, 0, -1):
            if str(i) in number[f_idx:]:
                idx = number.index(str(i))
                if idx <= (len_number - k):
                    f_idx = max(f_idx, idx)

        answer += number[f_idx]



    return answer


i_number, i_k = "1231234", 	3

print(solution(i_number, i_k))



