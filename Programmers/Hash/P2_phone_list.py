# 문제 설명
#
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
#     구조대 : 119
#     박준영 : 97 674 223
#     지영석 : 11 9552 4421
#
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
# 제한 사항
#
#     phone_book의 길이는 1 이상 1,000,000 이하입니다.
#         각 전화번호의 길이는 1 이상 20 이하입니다.
#         같은 전화번호가 중복해서 들어있지 않습니다.

# 한 번호가 통째로 다른 번호의 맨 앞에 순서대로 나열될 경우 이를 접두사라고 하고,
# 접두사가 발생하면 False를 출력한다.
# 먼저 폰북 리스트를 받아와서

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        p_len = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:p_len]:
            return False

    return True


phones = ["123","456","789"]

print(solution(phones))


def best_solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):       # 찾을문자열.startswith(시작문자, 시작지점) 을 사용하여 해당 문자가 있을경우 True를 아니면 False를 리턴
            return False
    return True

## 정석으로 해쉬 를 사용한 풀이.
def hash_solution(phone_book):
    answer = True
    hash_map = {}   # 해쉬맵 딕셔너리
    for phone_number in phone_book: # 폰북에서 각 넘버를 키로 하여 딕셔너리 작성
        hash_map[phone_number] = 1  # 벨류 1로 셋
    for phone_number in phone_book: # 처음 폰북 리스트로 반복문 수행
        temp = ""
        for number in phone_number: # 폰넘버 문자열을 한문자씩 받아옴
            temp += number          # 템프 문자열에 더해주면서
            if temp in hash_map and temp != phone_number:   #템프가 해쉬맵 안에 존재하고 현재 폰넘버와 다른 값인지 확인인
               answer = False
    return answer

