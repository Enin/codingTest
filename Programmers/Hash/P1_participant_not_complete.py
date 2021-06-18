# 해시란 Key-Value 쌍으로 데이터를 저장하는 자료구조이다.

# 완주하지 못한 선수
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#
#     마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
#     completion의 길이는 participant의 길이보다 1 작습니다.
#     참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
#     참가자 중에는 동명이인이 있을 수 있습니다.

# 1. 참가자 명단에서 한명씩 사람이름을 불러한다.
# 2. 완주한 사람 리스트에서 불러온 이름을 하나씩 비교하며 동일한 이름이 있을 경우 통과한다.
# 3. 만일 통과한 이름이 없을 경우 해당 이름을 return한다.

def solution(participant, completion):
    par_dict = {}
    for part in participant:
        if part in par_dict:
            par_dict[part] += 1
        else:
            par_dict[part] = 1

    for comp in completion:
        par_dict[comp] -= 1

    for key, value in par_dict.items():
        if value == 1:
            return key

p_list = ["mislav", "stanko", "mislav", "ana"]
c_list = ["stanko", "ana", "mislav"]
print(solution(p_list, c_list))

## best solution
from collections import Counter

def best_solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    print(answer)
    return list(answer.keys())[0]

print(best_solution(p_list, c_list))
