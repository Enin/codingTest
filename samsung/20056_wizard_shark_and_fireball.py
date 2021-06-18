# 어른상어가 마법사가 되어 파이어볼을 배움 ㅋㅋ
# nxn 격자에 파이어볼 m개를 발사한다. i번 파이어볼의 위치 ri, ci 질량 mi 방향 di 속력 si이다.
# 격자의 행과 열은 1번부터 n번까지 번호가 매겨지며 1번행은 n번행과 연결, 1번열은 n번열과 연결된다(이동가능)
# 파이어볼의 방향은 어떤 칸과 인접한 8개 칸
# 이동명령시 다음과같이 움직인다.
# 1. 모든 파이어볼이 자신의 방향 di로 속력 si 칸 만큼 이동 - 이동중 같은 칸에 여러개 파볼 가능
# 2. 이동이 끝나고 같은 칸에 2개 이상의 파볼이 있다면 다음 일이 발생
#   같은칸의 파볼이 모두 하나로
#   파볼이 4개로 나누어진다.
#       질량은 합쳐진 전체 질량 합 / 5 (소수점버림
#       속력 합쳐진 속력의 합 / 파볼 개수 (소수점버림
#       합쳐지는 파볼 방향이 모두 홀수이거나 짝수이면 방향은 0, 2, 4, 6이되고 그렇지 않으면 1, 3, 5, 7 로 나뉨
#   질량이 0인 파이어볼은 소멸됨
# k 번 이동명령 후 남아있는 파볼의 질량 합
from collections import deque
from copy import deepcopy


def fb_move(arr):    # 행, 열
    arr2 = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                q_len = len(arr[i][j])
                for q in range(q_len):
                    fm, fs, fd = arr2[i][j].popleft()  # 질량, 방향, 속도
                    nx, ny = i, j
                    for s in range(fs):
                        nx, ny = nx + dx[fd], ny + dy[fd]
                        if nx >= n and 0 <= ny < n:
                            nx = 0
                        elif nx < 0 and 0 <= ny < n:
                            nx = n-1
                        elif 0 <= nx < n and ny >= n:
                            ny = 0
                        elif 0 <= nx < n and ny < 0:
                            ny = n-1
                        elif nx == -1 and ny == -1:
                            nx, ny = n-1, n-1
                        elif nx == -1 and ny == n:
                            nx, ny = n-1, 0
                        elif nx == n and ny == -1:
                            nx, ny = 0, n-1
                        elif nx == n and ny == n:
                            nx, ny = 0, 0


                    arr2[nx][ny].append([fm, fs, fd])

    return arr2


def fb_div(arr):
    fm, fd, fs = 0, 0, 0
    arr2 = deepcopy(arr)

    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 1:
                f_len = len(arr[i][j])
                odd, even = 0, 0
                for _ in range(f_len):
                    m, s, d = arr2[i][j].popleft()
                    fm += m
                    fs += s
                    if d % 2 == 0:
                        even += 1
                    elif d % 2 == 1:
                        odd += 1

                nm = fm // 5
                if nm > 0:
                    ns = fs // f_len
                    if even == f_len:
                        dir_even = True
                    elif odd == f_len:
                        dir_even = True
                    else:
                        dir_even = False

                    for nd in range(4): # 0 1 2 3
                        if dir_even:
                            arr2[i][j].append([nm, ns, nd*2])
                        else:
                            arr2[i][j].append([nm, ns, nd*2+1])


            fm, fd, fs = 0, 0, 0

    return(arr2)


def fb_sum():
    total_sum = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for fm, _, _ in board[i][j]:
                    total_sum += fm

    return total_sum


def print_board(arr):
    print('_________')
    for i in range(n):
        print(arr[i])
    print('_________')

n, m, k = map(int, input().split()) # 보드크기, 파볼개수, 이동횟수
board = [[deque() for _ in range(n)] for _ in range(n)]  # n, n 행렬을 만듬. 각 칸에 [질량, 방향, 속도] 리스트를 항목으로 갖는 보드
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])

dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)

for _ in range(k):
    board = fb_move(board)
    board = fb_div(board)


print(fb_sum())

