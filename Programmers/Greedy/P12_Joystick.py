# 문제 설명
#
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
#
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
#
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
#
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
#
# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
#
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
# 제한 사항
#
#     name은 알파벳 대문자로만 이루어져 있습니다.
#     name의 길이는 1 이상 20 이하입니다.
def solution(name):
    answer = 0
    asciiA = ord('A')
    asciiZ = ord('Z')
    minAtoZ = (asciiZ - asciiA + 1)//2 + asciiA

    for str in name:
        asciiStr = ord(str)
        if asciiStr >= minAtoZ:  # 중간값 기준 위로할지 아래로할지.
            answer += asciiZ - asciiStr + 1
        else:
            answer += asciiStr - asciiA

    len_name = len(name)
    a_check = 0
    for str in name:
        if str == 'A':
            a_check = 1
            break

    if not a_check:
        min_case = len_name - 1

    else:
        Acomb = []
        idx = [0, 0, 0] # cnt, f_idx, b_idx

        for i, str in enumerate(name):
            if str == 'A':
                idx[0] += 1
                idx[2] = i
            else:
                idx[1] = idx[2] - idx[0] + 1
                Acomb.append(idx)
                idx = [0, 0, 0]

        Acomb = sorted(Acomb, key=lambda x: (-x[0]))
        _, f_idx, b_idx = Acomb.pop(0)

        if f_idx == 0:
            min_case = len_name - b_idx -1
        elif b_idx == len_name-1:
            min_case = f_idx - 1

        else:
            case1 = len_name - 1
            case2 = (len_name - b_idx - 1) + (f_idx - 1) * 2
            case3 = (len_name - b_idx - 1) * 2 + (f_idx - 1)
            min_case = min(case1, case2, case3)

    answer += min_case

    return answer

i_name = "ABBBAAAAABB"

print(solution(i_name))