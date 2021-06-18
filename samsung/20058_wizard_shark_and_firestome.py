# 2^n x 2^n 격자 djfdmavks
from itertools import chain
from collections import deque
from copy import deepcopy


n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int, input().split()))

dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1) # 북서남동

def print_board(board):
    for i in range(2**n):
        print(board[i])
    print('___________')


# l 크기 만큼 격자를 자름
# 나눈 부분 격자를 시계방향 90도 회전

def board_cut(cut): # 자를 크기 2**l 을 받아옴
    for i in range(0, 2**n, cut):   # i는 0부터 cut 크기 까지로 가져올 수 있음
        for j in range(0, 2**n, cut):     # board[i][j] 는 나눠진 격자의 첫번째 칸

            rotation(i, j, cut)


def rotation(cx, cy, cut): # 보드 좌표를 받은 뒤 cut 크기 기준으로 시계방향 1회전 수행
    temp = []
    for i in range(cut):
        temp.append(board[cx+i][cy:cy+cut])    # cy부터 cut까지 리스트를 세로로 cut 번 받아온다

    temp = rotated(temp)    # 90도 회전

    for i in range(cut):
        for j in range(cut):
            board[cx+i][cy+j] = temp[i][j]  # 보드 갱신



def rotated(arr_2d):
    list_o_tuples = zip(*arr_2d[::-1])
    return [list(e) for e in list_o_tuples]


def ice_melt(board):
    temp = deepcopy(board)
    for i in range(2**n):
        for j in range(2**n):
            if board[i][j] != 0:
                cnt = 0
                for d in range(4):  # 4방향 탐색
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < 2**n and 0 <= ny < 2**n and board[nx][ny] != 0:
                        cnt += 1

                if cnt < 3:
                    temp[i][j] -= 1
    return temp


def ice_sum():
    total_sum = sum(chain(*board))
    return total_sum


def ice_mess():
    max_mess = 0
    q = deque()
    visited = [[False]*(2**n) for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            if not visited[i][j] and board[i][j] != 0:
                q.append([i, j])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    cnt += 1
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < 2**n and 0 <= ny < 2**n and not visited[nx][ny] and board[nx][ny] != 0:
                            visited[nx][ny] = True
                            q.append([nx, ny])


                max_mess = max(max_mess, cnt)
                cnt = 0

    return max_mess
    #dfs 로 풀어도됨 >제일큰 덩어리니까 최대값

def ice_mess():
    max_mess = 0
    q = []
    visited = [[False]*(2**n) for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            if not visited[i][j] and board[i][j] != 0:
                q.append([i, j])
                visited[i][j] = True
                while q:
                    x, y = q.pop()
                    cnt += 1
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < 2**n and 0 <= ny < 2**n and not visited[nx][ny] and board[nx][ny] != 0:
                            visited[nx][ny] = True
                            q.append([nx, ny])


                max_mess = max(max_mess, cnt)
                cnt = 0

    return max_mess
    #dfs 로 풀어도됨 >제일큰 덩어리니까 최대값

def dfs(x, y):  # 좌표
    cnt = 0
    visited = [[False]*2**n for _ in range(2**n)]
    s = [[x, y]]
    for i in range(2**n):
        for j in range(2**n)
    while s:
        ex, ey = s.pop()
        for d in range(4):
            nx, ny = ex + dx[d], ey + dy[d]
            if 0 <= nx < 2**n and 0 <= ny < 2**n and board[nx][ny] != 0:
                s.append

    return cnt


for l in L:
    cut = 2 ** l
    board_cut(cut)
    board = ice_melt(board)


print(ice_sum())

mess = 0
for i in range(2**n):
    for j in range(2**n):
        if board[i][j] > 0:
            mess = max(mess, dfs(i, j))

print(mess)
