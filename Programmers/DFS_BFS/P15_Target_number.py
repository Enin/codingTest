#  타겟 넘버
#
# 문제 설명
#
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
#  예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
#  숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#
#     주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
#     각 숫자는 1 이상 50 이하인 자연수입니다.
#     타겟 넘버는 1 이상 1000 이하인 자연수입니다.

# 끝까지 탐색 > dfs 더하기 빼기의 2개 케이스로 나누어 스택-재귀 사용


case = []


def solution(numbers, target):
    dfs(numbers, target, 0, 0)

    return sum(case)


def dfs(l_numbers, target, made_number, cnt):
    if cnt==len(l_numbers):
        if made_number == target:
            case.append(1)

    else:
        dfs(l_numbers, target, made_number-l_numbers[cnt], cnt+1)
        dfs(l_numbers, target, made_number+l_numbers[cnt], cnt+1)


i_numbers, i_target = [1, 1, 1, 1, 1], 3

print(solution(i_numbers, i_target))


# 리스트 슬라이스를 이용

def best_solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])