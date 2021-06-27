#  가장 먼 노드
#
# 문제 설명
#
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다.
#  1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란
#  최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.
#
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
#  1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#
#     노드의 개수 n은 2 이상 20,000 이하입니다.
#     간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
#     vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.


# 최단경로로 이동했을때 간선 개수가 가장 많은 노드가 몇개인지 구하기.
# 1번 부터 출발해서 최단경로를 파악해야함. -> 동시 방문 가능하다면 동시에 방문을 표시한다.
# 간선 정보를 1에서 부터 오름차순으로 재정렬하고 popleft를 통해 1번 노드부터 확인을 수행.
# 더이상 움직일 수 없을때(연결된 노드가 모두 방문 상태일 경우) 이동한 횟수(cnt)를 이동리스트(level)에 저장한다.
# 모든 노드에 대해서 탐색을 종료한 다음 이동 리스트에서 최대값과 동일한 값으 횟수를 계산하고 return 한다.
from collections import deque, Counter
import heapq


def solution(n, edge):
    dict_graph = {x:[] for x in range(1, n+1)}
    distance = [float('inf')]*n
    distance[0] = 0
    for pre_node, next_node in edge:
        dict_graph[pre_node].append(next_node)
        dict_graph[next_node].append(pre_node)
    q = [1]
    heapq.heapify(q)

    while q:
        pre_node = heapq.heappop(q)
        for next_node in dict_graph[pre_node]:
            next_dist = distance[pre_node-1] + 1
            if distance[next_node-1] > next_dist:
                distance[next_node-1] = next_dist
                heapq.heappush(q, next_node)

    m_dist = max(distance)
    C_dist = Counter(distance)

    return C_dist[m_dist]


i_n, i_edge = 6, 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(i_n, i_edge))