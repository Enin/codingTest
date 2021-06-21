# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
#
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
#
#     array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
#     1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
#     2에서 나온 배열의 3번째 숫자는 5입니다.
#
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#
#     array의 길이는 1 이상 100 이하입니다.
#     array의 각 원소는 1 이상 100 이하입니다.
#     commands의 길이는 1 이상 50 이하입니다.
#     commands의 각 원소는 길이가 3입니다.

# 커맨드: [i:시작idx, j:끝idx, k:k번째수]


def solution(array, commands):
    answer = []

    for command in commands:
        slice_arr = array[(command[0]-1):(command[1])]
        slice_arr.sort()
        answer.append(slice_arr[(command[2]-1)])

    return answer


i_array, i_commands = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(i_array, i_commands))


# 람다식을 이용하여 구현한 형태.
def best_solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    # 커맨드를 x에 입력하고 arry의 command[0]-1:command[1] 까지를 sorted한 결과 리스트의 [x[2]-1]번째 값을 map으로 commands 전체로 수행한뒤 리스트로 리턴.