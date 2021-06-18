# We are given a set of integers and we have to find all the possible subsets of this set of integers.
# The following example elaborates on this further.
# subset의 전체 개수는 2^n 개 이다.
# 셋의 각 원소를 비트의 자리라고 생각하면 비트 시프트를 이용하여 각 원소의 조합을 구할 수 있다.

def get_all_subsets(v):
    subsets = []

    for i in range(1<<len(v)):  # 2^n, i는 입력된 세트에서 값의 위치들을 표시.
        temp_set = set([])
        for j in range(len(v)): # j는 한비트씩 이동하면서(temp) i가 가리키는 위치들과 비교하여 같은 위치에 1이 있을때 해당 위치의 값을 세트에 저장.
            print('i: {}, j: {}'.format(i,j))
            temp = i & (1<<j)   # i와 2^j승을 비교하여 동일하면 temp에 값이 저장됨 0011 & 0100
            print('temp:', temp)
            if temp:            # temp 가 0이 아닐 경우(i와 2^j 가 같을 경우)
                temp_set.add(v[j])  # 임시 셋에 j번째 값을 저장
            print(temp_set)

        subsets.append(list(temp_set))
        print('subset:', subsets)

    return subsets





    return subsets

if __name__ == '__main__':
    input_set = [1, 2, 3, 4]
    print(get_all_subsets(input_set))
