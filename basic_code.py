# from random import *  # 랜덤 함수 사용 라이브러리
#
# print(int(random() * 10) + 1)  # 1에서 부터 10사이의 랜덤 int 1개를 출력
# print(randint(1, 45))  # 1~45 사이의 랜덤 int 1개를 출력
#
# name = "lee"
# print(name[2])  # 문자열은 리스트처럼 n번째 문자를 가져올 수 있음.
#
# print("Lol".lower())  # 소문자로 변경
# print("Lol".upper())  # 소문자로 변경
# x = "lol"
# print(x.replace("lo", "ro"))  # lo 부분을 ro 로 변경
# y = x.index("o")  # o가 처음 등장할때 몇번째 위치에 있는지 알려줌
# print(y)
# y = x.index("l", y + 1)  # 다음 위치의 l을 출력
# print(y)
# print(x.find("l"))  # index와 비슷하며 없을 경우 -1을 반환. index에서는 에러를 출력함.
#
# list_1 = ["가", "나", "다"]
# print(list_1.index("나"))  # 인덱스: 위치찾기
# list_1.insert(list_1.index("나"), "라")  # 인설트 해당 위치 뒤에 삽입.
# print(list_1)
# print(list_1.count("가"))  # 가 의 숫자 세기
num_list = [2, 5, 1, 2, 4]
num_list.sort()  # 순서대로 정렬
print(num_list)
num_list.reverse()  # 순서 뒤집기
print(num_list)  # .clear는 내용을 모두 지움.
mix_list = ["가", 20, True]
num_list.extend(mix_list)  # 두 리스트를 합침.
print(num_list)

dict1 = {"키1": 1, "키2": 2}
print(dict1)
dict1["키3"] = 3  # 키와 데이터 업데이트
print(dict1)  # 키값에 접근할때는 딕셔너리[키]를 사용한다. 키가 없을경우 새로운 키를 생성한다.
print(dict1.keys())  # 키만 출력. .value() 벨류만 출력. .items() 키,벨류 쌍 출력
del dict1["키1"]  # 해당 키를 삭제

tuple1 = ("돈", "가스")  # 튜플은 ()를 사용한다. 튜플 특징은 데이터 값을 변경할 수 없음. - 고정값

# set : 집합. 중복이 안되며 순서가 없다.
set1 = {1, 2, 3, 4, 3, 3}
print(set1) # 중복되는 3은 무시됨

# set 연산자: & intersection(), | union(), - difference(), + add(), 제거 remove()
# list(), set(), tuple()은 각각 변경할 수 있다. 딕셔너리는 안됨.

users = list(range(1, 21))  # range 범위의 1단위로 늘어나는 값을 리스트로 생성

list1 = [1,2,3,4,5]
print(max(list1))

print((3 + 2) // 2) # 나누고 나머지는 버림

import math
print(math.sqrt(9)) # 루트
print(math.pow(3, 2))   # 거듭제곱
print(2**2)

# sorted() 함수. 리스트를 정렬하고 반환