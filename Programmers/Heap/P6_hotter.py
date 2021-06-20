# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
#
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
#
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
# 제한 사항
#
#     scoville의 길이는 2 이상 1,000,000 이하입니다.
#     K는 0 이상 1,000,000,000 이하입니다.
#     scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
#     모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
import heapq


def solution(scoville, K):
    answer = 0
    # 입력 스코빌을 최소힙 정렬한다. .heapify(리스트) 로 최소힙 자료형으로 만들어줌
    heapq.heapify(scoville)

    while True:
        low_s = heapq.heappop(scoville)  # 수행하면 가장 낮은 값을 리턴한다.
        # 현재 가장 낮은 값이 K 이상이라면 동작을 종료하고 섞은 횟수를 리턴한다.
        if low_s >= K:
            return answer
        # 위 조건을 만족하지 않는 경우 섞기 작업을 수행한다.
        else:
            if not scoville:    # low_s 가 남아있는 마지막 요소라면 더이상 scoville에 값이 남아있지 않아 heappop을 할 수 없다. return -1로 탈출.
                return -1
            low_s2 = heapq.heappop(scoville)    # 다음으로 낮은 값을 출력
            new_s = low_s + (low_s2 * 2)
            heapq.heappush(scoville, new_s) # 새로운 매운음식을 만들고 힙에 입력한다.

            answer += 1 # 섞은 횟수를 증가시키고 while문 처음으로 돌아간다.


i_scoville = [1, 2, 3, 9, 10, 12]
i_k = 7

print(solution(i_scoville, i_k))


