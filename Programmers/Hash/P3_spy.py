# 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
#
# 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면
# 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
# 종류 	이름
# 얼굴 	동그란 안경, 검정 선글라스
# 상의 	파란색 티셔츠
# 하의 	청바지
# 겉옷 	긴 코트
#
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#
#     clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
#     스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
#     같은 이름을 가진 의상은 존재하지 않습니다.
#     clothes의 모든 원소는 문자열로 이루어져 있습니다.
#     모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
#     스파이는 하루에 최소 한 개의 의상은 입습니다.

# 의상이름-key, 의상종류-value로 딕셔너리 생성
def first_solution(clothes):
    # dict_cloths = {}
    # answer = 0
    # 딕셔너리 안쓰고 그대로
    # for i, cloth in enumerate(clothes):
    #     dict_cloths[i] = cloth[1]

    cloths_number = len(clothes)
    cloth_combination = []

    for i in range(1 << cloths_number):
        comb_temp = []
        kind_temp = []
        for j in range(cloths_number):
            if i & (1 << j):
                if clothes[j][1] not in kind_temp:
                    kind_temp.append(clothes[j][1])
                    comb_temp.append(j)

        if comb_temp not in cloth_combination:
            cloth_combination.append(comb_temp)

    print(cloth_combination)
    cloth_combination.pop(0)
    answer = len(cloth_combination)

    return answer

    # for comb in cloth_combination:
    #     cnt = Counter(comb)
    #     max_value = max(list(cnt.values()))
    #     if max_value >= 2:
    #         answer -= 1

def solution(clothes): # best solution
    # 옷의 종류별로 (옷종류갯수+벗은상황)*(옷종류갯수+벗은상황1)*... - 1(아무것도 안입었을때
    # 종류(키): 옷(벨류) 로 딕셔너리 생성
    # 각 딕셔너리 항목별 갯수+1을 다 곱해주고 마지막에 - 1
    answer = 1
    dic = {}
    for cloth, ctype in clothes:
        if not dic.get(ctype):
            dic[ctype] = [cloth]
        else:
            dic[ctype].append(cloth)

    for c_type in dic:
        answer *= len(dic[c_type]) + 1

    return answer - 1



p_list = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(p_list))


def best_solution(clothes):
    from collections import Counter
    from functools import reduce    # reduce(집계함수, 순회가능 데이터,[,초기값]) 집계함수는 lambda 누적자(x,y): 집계함수(x*(y+1)), 순회데이터, 초기값) 형태
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer