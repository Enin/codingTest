## https://www.acmicpc.net/problem/2805
# 나무자르기 문제
# 이분탐색 문제
N, M = map(int, input().split())
T = list(map(int, input().split()))
low, high = 1, max(T)

while low <= high:      # high가 low보다 작아지면 반복을 종료. 이때 high가 M을 구할수있는 최고 높이가 된다.
    mid = (low + high) // 2
    H = 0
    for i in T:
        if i > mid:
            H += i - mid

    if H == M:          # H가 M과 바로 같을 경우에는 탈출 mid를 바로 출력하고 탈출문으로 빠져나온다.
        print(mid)      # 이 조건을 안 넣으면 시간초과가 나옴.
        exit()

    elif H >= M:
        low = mid + 1   # 잘린 나무의 합이 M보다 크면 높이를 올려서 크기를 M에 가깝게 줄여나간다.

    else:               # 반대로 H가 M보다 작다면 높이를 낮춰서 평균값을 아래로 내린다.
        high = mid - 1  # 먼저 위로 올라갔다가 아래로 다시 내려오면서 맞는값을 찾게됨

print(high)             # 최종적으로 최소화된 high가 결과값을 가짐

