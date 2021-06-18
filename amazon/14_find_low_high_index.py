# Given a sorted array of integers, return the low and high index of the given key.
# You must return -1 if the indexes are not found.
# The array length can be in the millions with many duplicates.
# 정렬된 인테저 어레이가 주어지고, 주어진 키의 하이/로우 인덱스를 리턴하는 함수만들기.
# 이때 주어진 키와 동일한 값이 없으면(인덱스가 없으면) -1을 리턴.
# 투포인터로 접근하면 좋을듯하다.
# 예시: 0, 1, 1, 1, 2, 3, 4, 4, 5 일때 키가 1이면 low: 1, high: 3이 된다.

# 주어진 답안
# 바이너리 서치를 사용함.
# 미들을 기준으로 low 와 high 포인터를 만든다.


def find_low_index(arr, key):
    try:
        return arr.index(key)
    except ValueError:
        return -1


def find_high_index(arr, key):
    rev_arr= arr[::-1]
    try:
        return len(arr) - rev_arr.index(key) - 1
    except ValueError:
        return -1


def find_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = int(high / 2)

    while low <= high:

        mid_elem = arr[mid]

        if mid_elem < key:
            low = mid + 1
        else:
            high = mid - 1

        mid = low + int((high - low) / 2)

    if low < len(arr) and arr[low] == key:
        return low

    if high == -1:
        return high

    if high < len(arr) and arr[high] == key:
        return high

    return -1


def test(arr, key):
    low_index = find_low_index(arr, key)
    high_index = find_high_index(arr, key)

    print('key {} / low index: {}, high index: {}'.format(key, low_index, high_index))




if __name__ == '__main__':
    sorted_arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    key = 1
    print('input arr:', sorted_arr)
    test(sorted_arr, key)