# https://www.acmicpc.net/problem/2003
# 수의 합 2번 문제
import time
#
# start = time.time()
#
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# start = time.time()
# cnt = 0
#
# for i in range(N):
#     if A[i] == M:
#         cnt += 1
#         continue
#     for j in range(i, N):
#         if sum(A[i:j+1]) == M:
#             cnt +=1
#
# print(cnt)
#
# end = time.time()
#
# print('start: %s' % start)
# print("end: %s" % end)
# print("take time: %s" % (end - start))


## 풀이
# 위와 같이 수행할 경우 수가 커지면 시간 복잡도가 N^2가 되어 비효율적이다.
# 이 같은 문제를 해결하려면 투포인터 알고리즘을 사용해야 한다.

# N, M = map(int, input().split())
# sumA = [0]   # A의 리스트 합을 저장하기 위해 sum_A 리스트 생성. start=0, end=1 일때를 고려하여 N+1개 생성함
# a = 0
# A = map (int, input().split())
# for i in A:
#     a += i
#     sumA.append(a)
# cnt = 0
# for end in range(len(sumA)):
#     if sumA[end] >= M:        # sumA[end]의 값이 M보다 크거나 같다면 sumA[start]를 빼서 M과 같게 만들 수 있다.
#         for start in range(end):   # 2중 for문으로 start, end 포인터를 이동시키며 조건을 확인.
#             if sumA[end] - sumA[start] == M:
#                 cnt += 1
#                 break
#             elif sumA[end] - sumA[start] < M:
#                 break
# print(cnt)

## 풀이 2
# 0번과 1번을 혼합
# 투포인터 알고리즘

N, M = map(int, input().split())
A = list(map(int, input().split()))
sumA = 0
cnt = 0
start = 0
for end in A:
    sumA += end   # sumA에 현재 합계를 계산
    if sumA >= M:   # A의 합계가 M보다 클 경우 start 포인터를 이동하면서 부분합을 빼줌.
        while sumA >= M:    # 합계가 M보다 작아질때 까지 루프문 반복.
            if sumA == M:
                cnt += 1
            sumA -= A[start]    # A를 하나씩 빼면서 M보다 작아지는 것을 확인.
            start += 1  # 한번 나온다음에 그다음 end에 뺄 start 는 0부터 시작할 필요없이 이전 start에서 이어서 수행한다.
print(cnt)