#

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 1, 0, -1), (-1, 0, 1, 0)   # 서 남 동 북
dx2, dy2 = (-1, 1, 1, -1), (-1, -1, 1, 1) # 북서 남서 남동 북동
out_board = 0

def print_board(board):
    global out_board
    print('out:', out_board)
    for i in range(n):
        print(board[i])

    print('___________')

# 토네이도 이동을 확인
def t_move(tx, ty, td, num, cnt):    # 토네이도 행, 열, 방향, 움직인 횟수
    nx, ny = tx, ty
    for _ in range(num):
        nx, ny = nx + dx[td], ny + dy[td]

        dust_flow(nx, ny, td)
        if nx == 0 and ny == 0:
            return None, None, None, None, None

    cnt += 1
    td = (td + 1) % 4
    return nx, ny, td, num, cnt


# 모래 날리는것을 확인
def dust_flow(tx, ty, td):  # 토네이도 행, 열, 방향 이때 토네이도 위치는 이동된 위치y
    global out_board
    origin = board[tx][ty]  # y 위치의 값을 임시 저장
    board[tx][ty] = 0
    per_10 = (origin * 10) // 100
    per_7 = (origin * 7) // 100
    per_5 = (origin * 5) // 100
    per_2 = (origin * 2) // 100
    per_1 = (origin * 1) // 100
    alpha = origin - 2 * (per_10 + per_7 + per_2 + per_1) - per_5   # 북쪽: td 3 dx dy -1 0
    nx_list = [[tx + dx[td] * 2, ty + dy[td] * 2, per_5],
               [tx + dx2[td], ty + dy2[td], per_10],
               [tx + dx2[(td+1)%4], ty + dy2[(td+1)%4], per_10],
               [tx + dx[(td - 1) % 4], ty + dy[(td - 1) % 4], per_7],
               [tx + dx[(td + 1) % 4], ty + dy[(td + 1) % 4], per_7],
               [tx + dx[(td - 1) % 4] * 2, ty + dy[(td - 1) % 4] * 2, per_2],
               [tx + dx[(td + 1) % 4] * 2, ty + dy[(td + 1) % 4] * 2, per_2],
               [tx + dx2[(td - 1) % 4], ty + dy2[(td - 1) % 4], per_1],
               [tx + dx2[(td + 2) % 4], ty + dy2[(td + 2) % 4], per_1],
               [tx + dx[td], ty + dy[td], alpha]]

    for fx, fy, value in nx_list:
        if 0 <= fx < n and 0 <= fy < n:
            board[fx][fy] += value

        else:
            out_board += value




ox, oy = n // 2, n // 2   # 중심좌표에서 시작
od = 0
o_num, o_cnt = 1, 0

while True:

    if o_cnt == 2:
        o_cnt = 0
        o_num += 1
    ox, oy, od, o_num, o_cnt = t_move(ox, oy, od, o_num, o_cnt) # cnt가 2가되면 0으로 초기화시키고 num을 +1
    if ox is None:
        break



print(out_board)






