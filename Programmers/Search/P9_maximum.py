# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
# 제한 사항
#
#     numbers의 길이는 1 이상 100,000 이하입니다.
#     numbers의 원소는 0 이상 1,000 이하입니다.
#     정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# 정수 리스트를 입력받고 그중 가장 큰 수를 만들어내기.

# 주어진 정수에 대해 가장 왼쪽자리 수가 무엇인지 저장하자.
# 왼쪽자리수를 기준으로 정렬을 하면 저음에 올 가장 큰 수를 구할 수 있을것이다.
# 퍼뮤테이션을 만들고

from itertools import permutations
import heapq

def solution(numbers):
    answer = ''
    temp_num = []
    for num in numbers:
        temp = num
        while temp <= 100:
            if temp == 0:
                break
            temp *= 10

        temp_num.append((temp, num))
    temp_num.sort(key=lambda x: (x[0], -x[1]),reverse=True)
    print(temp_num)
    for _, num in temp_num:
        answer += str(num)

    return answer


i_numbers = [3, 30, 31, 25, 9, 0]

print(solution(i_numbers))