import sys
from collections import deque
import copy
#f = open('15684.txt','r')
M, num, N = list(map(int, input().split(' ')))

# How to make graph?
# (r,c)에서 오른쪽으로 넘어가려면 graph[r][c] = 1 , 왼쪽으로 넘어가려면 graph[r][c-1] = 1
graph = [[0]*(M) for i in range(N)]
for i in range(num):
    r, c = list(map(int, input().split(' ')))
    graph[r-1][c-1] = 1

# Find 0인 지점.
zero_lines = []
for r in range(N):
    for c in range(M-1):
        if graph[r][c] == 0:
            zero_lines.append( (r,c) )



'''
for i in range(N):
    print(graph[i])
print(zero_lines)
'''

# 위에서 아래로 이동
def move(graph):
    # One
    count = 0
    for c_ in range(M):
        r = 0
        c = c_
        # 조건1. 맨 아래까지 갈때까지
        while r != N: # N-1?
            if c == 0: # 맨 왼쪽
                if graph[r][c] == 1:
                    r = r+1
                    c = c+1
                else:
                    r = r+1
                    c = c
            elif c == M-1: # 맨 오른쪽
                if graph[r][c-1] == 1:
                    r = r+1
                    c = c-1
                else:
                    r = r+1
                    c = c
            else:
                if graph[r][c] == 1:
                    r = r+1
                    c = c+1
                elif graph[r][c-1] == 1:
                    r = r+1
                    c = c-1
                else:
                    r = r+1
                    c = c
        if c != c_:
            count = count + 1
    return count

# 가로선 추가
def add_line(graph, r, c):
    # 조건3. 연속 or 접X
    if M == 2:
        graph[r][c] = 1
        return graph, 1
    else:
        if c == 0:
            if graph[r][c+1] == 1:
                return graph, -1
            else:
                graph[r][c] = 1
                return graph, 1
        elif c == M-2:
            if graph[r][c-1] == 1:
                return graph, -1
            else:
                graph[r][c] = 1
                return graph, 1
        else:
            if graph[r][c-1] == 1 or graph[r][c+1] == 1:
                return graph, -1
            else:
                graph[r][c] = 1
                return graph, 1

def bfs(graph, zero_lines):
    # 하나도 필요없는 경우.
    if move(graph) == 0:  # 정답
        return print(0)
    # Define queue
    queue = deque([(graph, [],0)]) # ( 그래프, 추가한점들, 횟수)

    # queue가 다 없어질 때까지
    while queue:
        # print(queue)
        graph_, points, count = queue.popleft()
        # 가로선추가
        for r, c in zero_lines:
            if (r,c) not in points:
                graph__ = copy.deepcopy(graph_)
                graph__, pos = add_line(graph__, r, c)
                # 조건. 가로선 인접 X
                if pos:
                    # 조건. 정답이 나오는지
                    wrong_count = move(graph__)
                    if wrong_count == 0: # 정답이면
                        return print(count+1)
                    elif 1 <= wrong_count <= 2 and count + 1 <= 2:
                        queue.append( (graph__, points + [(r,c)],count + 1) )
                        print(points + [(r,c)])
                    elif 3 <= wrong_count <= 4 and count + 1 == 1:
                        queue.append((graph__, points + [(r, c)], count + 1))
    return print(-1)

bfs(graph, zero_lines)