#  입국심사
#
# 문제 설명
#
# n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
#
# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
#  가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다.
#  하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
#
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
#
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때,
#  모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#
#     입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
#     각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
#     심사관은 1명 이상 100,000명 이하입니다.

# times 는 심사관마다 1명 심사에 걸리는 시간.
# 심사 받을 사람은 n명 존재한다.
# 가장 앞사람은 종료시간이 빠른 심사대에서 심사를 본다.
# 모든 사람들이 심사를 받을때 걸리는 시간이 최소.
# 이분탐색을 사용?

# 심사관마다 심사 종료되는 타임을
import heapq


# def solution(n, times):
#     answer = 0
#     times.sort()
#     immig = []
#     len_times = len(times)
#     for i in times:
#         immig.append([i, i])
#
#     bs_l, bs_r, bs_m = 0, len_times-1, len_times//2   # 초기 bs 왼쪽 오른쪽 위치.
#
#     for i in range(n):
#         immigration_time, origin_time = immig.pop(0)
#         answer = immigration_time
#
#         while bs_l < bs_r:
#             if bs_m > immigration_time:
#                 bs_r = bs_m - 1
#                 bs_m = (bs_r - bs_l) // 2
#             elif bs_m < immigration_time:
#                 bs_l = bs_m + 1
#                 bs_m = (bs_r - bs_l) // 2
#
#         next_immigration = immigration_time + origin_time
#         if immig[bs_m][0] < next_immigration:
#             immig.append([next_immigration, origin_time])
#         else:
#             immig.insert(bs_m, [next_immigration, origin_time])
#
#     return answer



import heapq


# def solution(n, times):
#     answer = 0
#     immig = []
#     for i in times:
#         immig.append([i, i])
#
#     heapq.heapify(immig)
#
#     for i in range(n):
#         immigration_time, origin_time = heapq.heappop(immig)
#
#         answer = immigration_time
#
#         heapq.heappush(immig, [immigration_time+origin_time, origin_time])
#
#     return answer

def solution(n, times):
    i = 50
    t = 0
    while i > 0:
        i -= 1
        temp = t + 2**i
        cnt = 0
        for time in times:
            cnt += temp//time
        if cnt >= n:
            cnt1 = 0
            for time in times:
                cnt1 += (temp-1)//time
            if cnt1 < n:
                return temp
        else:
            t = temp
    return t

i_n, i_times = 6, [7, 10]

print(solution(i_n, i_times))
