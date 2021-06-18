# Search for a given number in a sorted array, with unique elements,
# that has been rotated by some arbitrary number.
# Return -1 if the number does not exist.
# Assume that the array does not contain duplicates.
# rotated된 정렬 어레이에서 주어진 숫자를 탐색하는 함수를 구현하기.
# 이때 엘리멘트는 arbitrary 넘버로 회전하는 요소이다.
# 숫자가 없을때는 -1을 반환한다.
# 어레이는 중복값을 갖지 않는다.

# 파이썬에서는 사실 list.index(key)를 사용하여 손쉽게 값을 구할 수 있다.
# 14번과 동일하게 바이너리 서치를 구현하되, 로테이션 함수를 추가할것.
# 바이너리 서치 알고리즘과 함께 제일 큰 값을 기준으로 양쪽이 이미 정렬되어 있다는 점을 이용하면 된다.
# 솔찍히 파이썬이면 걍 인서트 쓰면되는데 ㅠㅠ


def binary_search_rotated(arr, key):
    low = 0
    high = len(arr) - 1


    while True:

        if low > high:
            return -1

        mid = int(low + (high - low) / 2)
        print(arr[low], arr[mid], arr[high])
        print(low, mid, high)
        if arr[mid] == key:
            return mid + 1

        elif arr[low] <= arr[mid] and arr[mid] >= key >= arr[low]:
            high = mid - 1
            print('a')

        elif arr[mid] <= arr[high] and arr[high] >= key >= arr[mid]:
            low = mid + 1
            print('b')

        elif arr[mid] >= arr[high]:
            low = mid + 1
            print('d')

        elif arr[mid] <= arr[low]:
            high = mid - 1
            print('c')

        else:
            return  -1

        print('loop')
# [15,20,430,600,1,3,4,6,7,10]


def array_rotation(arr, num):
    max = len(arr)
    if num == max:
        return arr

    elif num > max:
        num -= max

    rotated_arr = arr[max-num:] + arr[:max-num]
    print('array rotate:', rotated_arr)
    return rotated_arr


if __name__ == '__main__':

    arr = [1,3,4,6,7,10,15,20,430,600]
    rotate = 6
    select_num = 1

    print('input array: ', arr)
    result = binary_search_rotated(array_rotation(arr, rotate), select_num)
    print('find key: ', select_num, 'key rocation: ', result)


def binary_search_rotated_rec(arr, low, high, key):

    if low > high:
        return -1

    mid = int(low + (high - low) / 2)
    print(arr[low], arr[mid], arr[high])
    if arr[mid] == key:
        return mid + 1

    elif arr[low] <= arr[mid] and arr[mid] >= key >= arr[low]:
        return binary_search_rotated_rec(arr, low, mid - 1, key)

    elif arr[mid] <= arr[high] and arr[high] >= key >= arr[mid]:
        low = mid + 1
        return binary_search_rotated_rec(arr, mid + 1, high, key)

    elif arr[mid] <= arr[low]:
        return binary_search_rotated_rec(arr, low, mid - 1, key)

    elif arr[mid] >= arr[high]:
        return binary_search_rotated_rec(arr, mid + 1, high, key)

    return -1


def binary_search_rotated(arr, key):
    return binary_search_rotated_rec(arr, 0, len(arr) - 1, key)