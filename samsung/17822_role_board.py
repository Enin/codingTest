from collections import deque
from itertools import chain


def rotation(x, d, k):  # x번째 원판, 방향d(0:시계, 1:반시계), k 칸 이동
    if d == 0:
        k = m - k
    for xi in range(x, n+1, x):
        board[xi-1] = board[xi-1][k:] + board[xi-1][:k]


def bfs(map, x, y):
    q = deque()
    value = map[x][y]   # 현 좌표의 값
    q.append([x, y])
    visited = set()    # 방문 여부
    while q:
        x, y = q.popleft()
        visited.add((x, y))
        for dirs in range(4):  # 4방향 탐색
            nx, ny = x + dx[dirs], y + dy[dirs]
            if ny < 0: ny = m - 1   # 0 의 다음은 n-1
            if ny >= m: ny = 0      # n-1 다음은 0
            if 0 <= nx < n and map[nx][ny] == value and (nx, ny) not in visited:    # 범위안 + 방문 안했을때
                q.append([nx, ny])
                visited.add((nx, ny))

    return visited  # 현 좌표에서 방문 가능한 리스트를 출력.


def calc(map):
    is_adj = False  # 제거 가능한 수가 있는지 판별

    for i in range(n):
        for j in range(m):
            current = map[i][j]
            if current == 0: continue   # 이미 0이 된 경우에는 통과
            adj = bfs(map, i, j)    # 방문 가능 여부 확인. 방문한 리스트를 반환.
            if len(adj) > 1: # adj가 존재할 경우
                is_adj = True
                for ni, nj in adj:
                    map[ni][nj] = 0 # 좌표를 받아온 뒤 모두 0으로 변경
    # 모두 방문했지만 인접항목 제거를 하지 못했을 경우. 모든 수가 0이라면 리스트에 아무것도 없어서 걸러진다.
    remain = [i for i in chain(*map) if i != 0] # chain은 iter 가능한 것들을 하나로 연결해준다. *map으로 map을 한꺼풀 벗겨서 가져옴.
    if not is_adj and remain:   # remain이 없으면 걸러짐
        avg = sum(remain) / len(remain)
        for i in range(n):
            for j in range(m):
                if map[i][j] != 0 and map[i][j] > avg: map[i][j] -= 1
                elif map[i][j] != 0 and map[i][j] < avg: map[i][j] += 1


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = (-1, 0, 1, 0), (0, 1, 0 , -1)

    for i in range(t):
        x, d, k = map(int, input().split())
        rotation(x, d, k)
        calc(board)

    print(sum(chain(*board)))
