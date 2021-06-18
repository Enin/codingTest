# 16진수 1자리는 2진수 4자리로 표시된다.
#
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
#
# 단, 2진수의 앞자리 0도 반드시 출력한다.
#
# 예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

def binary1():
    t = int(input())

    for i in range(1, t + 1):
        n, a = input().split()
        result = ''
        for j in range(int(n)):
            result += '{:04b}'.format(int(a[j], 16))
        print('#{} {}'.format(i, result))


# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.
#
# N = 0.625
# 0.101 (이진수)
# = 1*2-1 + 0*2-2 + 1*2-3
# = 0.5 + 0 + 0.125
# = 0.625
#
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
# 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

def binary2():
    T = int(input())

    for case in range(1, T+1):
        data = float(input())
        result = ''
        count = 1
        while count < 13:
            data *= 2
            result += str(int(data) % 2)
            if data % 1 == 0:
                break
            count += 1
        else:
            result = 'overflow'

        print('#{} {}'.format(case, result))





