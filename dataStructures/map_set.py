# 맵은 딕셔너리로 구현되어 있음.
dict1 = {'kim': 12, 'lee': 14, 'park': 16}

print(dict1['kim'])

del dict1['kim']

print(dict1)

dict1['yun'] = 15
print(dict1)

# 키만 자료형으로 만들 수 있다.
key_list = dict1.keys()
print(key_list)
k_list = list(key_list)
print(type(k_list))

# 셋은 키가 없는 딕셔너리로 사용
set1 = {1, 2, 3, 4}
set1.update({2, 5, 8, 9})   # 순서대로 입력
print(set1)
