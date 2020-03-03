## 피보나치 수열 문제
# 재귀함수 사용

n = int(input())


def fibonacci(N):
    F = []
    for i in range(N + 1):
        if i == 0:
            F.append(0)
        elif i == 1:
            F.append(1)
        else:
            F.append(F[i - 1] + F[i - 2])
    return F


result = fibonacci(n)

print(result[-1])

## 풀이
# 좀더 간단하게 단축할 수 있다.
# 수열을 저장하지 않고 F0, F1을 하나씩 앞으로 가면서 갱신시키는 방법으로 출력 가능하다.

F0, F1 = 0, 1  # 먼저 F0, F1의 조건을 지정한다.
for i in range(n):
    F0, F1 = F1, F0 + F1  # 피보나치 수열을 한칸씩 앞으로 보내면서 F0와 F1을 갱신한다.
    # N번 수행할 경우 F0가 N번째 값이 되며 F1은 N+1번째 값이 된다.
print(F0)

## 풀이2
# 피보나치 공식을 사용하면 마지막 값을 바로 구할 수도 있다.
import math


def fibo_fn(n):
    Fn = ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / ((2 ** n) * math.sqrt(5))
    return Fn


print(fibo_fn(n))

