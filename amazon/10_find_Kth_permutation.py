# Given a set of ‘n’ elements, find their Kth permutation.
# Consider the following set of elements:
import itertools

def factor(n):
    if n == 0 or n == 1:
        return 1
    return n * factor(n - 1)


def find_kth_permutation_use_itertools(v, k):
    if not v:
        return
    result = []
    for i in list(itertools.permutations(v)):
        result.append(i)
    print('total permutaion number is {}'.format(len(result)))

    return result[k]

def find_kth_permutation(v, k, result):
    if not v:
        return

def get_permutation(v, n):
    result = []
    k = len(v)
    if n > k:
        return result

    if n == 1:
        for i in v:
            result.append([i])

    elif n > 1:
        for i in range(k):
            temp = [j for j in v]
            print('temp {}'.format(temp))
            temp.remove(v[i])
            print(temp)
            for p in get_permutation(temp, n-1):
                print('p {}'.format([p]))
                result.append([v[i]]+p)

    print('middle: {}'.format(result))
    return result




def test(n, k):
    v = list(range(1, n+1))
    # result = find_kth_permutation_use_itertools(v, k-1)
    # result = ''.join(map(str, result))
    # print('{}th permutaion result is {}'.format(k, result))

    result2 = get_permutation(v, len(v))
    print('result2 {}'.format(result2))


if __name__ == '__main__':
    test(3, 4)
