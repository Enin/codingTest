from itertools import chain


def move(t, x, y, board, is_g):
    c = y
    if not is_g:
        c = x
        if t == 2:
            t = 3
        elif t == 3:
            t = 2
    pos = 0
    if t == 1:
        while pos < 5 and board[pos+1][c] != 1:
            pos += 1
        board[pos][c] = 1
    elif t == 2:
        while pos < 5 and board[pos+1][c] != 1 and board[pos+1][c+1] != 1:
            pos += 1
        board[pos][c] = 1
        board[pos][c+1] = 1
    elif t == 3:
        while pos < 5 and board[pos+1][c] != 1:
            pos += 1
        board[pos][c] = 1
        board[pos-1][c] = 1

def erase_row(board):
    point = 0
    for i in range(6):
        if board[i] == [1, 1, 1, 1]:    # 완성 되었을때
            point += 1   # 초기화
            for j in range(i, 0, -1):   # 역순으로 이동
                board[j] = board[j-1]
            board[0] = [0, 0, 0, 0]     # 0번째는 0이 들어감

    while board[1] != [0, 0, 0, 0]: # 1번 보드 줄이 비어있지 않을 때까지 수행
        for i in range(5, 0, -1):   # 5번행부터 차례로 한행씩 아래로 내려줌
            board[i] = board[i-1]
        board[0] = [0, 0, 0, 0]     # 마지막 행은 0으로 초기화

    return point


def board_sum(board):
    sum_out = sum(chain(*board))
    return sum_out


def print_board(board):
    print()
    for i in range(6):
        print(board[i])
    print('_______________')


board_b = [[0]*4 for _ in range(6)]
board_g = [[0]*4 for _ in range(6)] # 입력할때 transpose 하면 됨.
total_ans = 0

n = int(input())
for i in range(n):
    t, x, y = map(int, input().split()) # t가 1, 2, 3일때 조건을 각각 만든다.

    move(t, x, y, board_b, False)
    move(t, x, y, board_g, True)

    b_point = erase_row(board_b)
    g_point = erase_row(board_g)

    total_ans = total_ans + b_point + g_point


print(total_ans)
print(board_sum(board_b) + board_sum(board_g))
