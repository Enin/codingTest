# 최소합
# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
#
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
#
# 1   2   3
# 2   3   4
# 3   4   5
#
# 그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

def min_addition():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())
        board = []
        for i in range(N):
            row = list(map(int, input().split()))
            board.append(row)

        result_board = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                result_board[i][j] = board[i][j]
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    result_board[i][j] += result_board[i][j-1]
                elif j == 0:
                    result_board[i][j] += result_board[i-1][j]
                if i != 0 and j != 0:
                    row_ = result_board[i-1][j]
                    col_ = result_board[i][j-1]
                    if row_ < col_:
                        result_board[i][j] += row_
                    else:
                        result_board[i][j] += col_

        print('#{} {}'.format(case, result_board[-1][-1]))

# 완전검색 - 전자카트
# 골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
#
# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.
#
# 각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
#
# 두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.
#
# N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
#
# e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
#
# e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89
#
# e   1   2   3   도착
# 1   0   18  34
# 2   48  0   55
# 3   18  7   0
#
# 이 경우 최소 소비량은 89가 된다.

import itertools
def cart():
    T = int(input())

    for case in range(1, T+1):
        N = int(input())
        N_perm = itertools.permutations([i for i in range(1, N+1)])
        course = []
        for x in N_perm:
            if x[0] == 1:
                course.append(list(x)+[1])
        board = []
        for i in range(N):
            board.append(list(map(int, input().split())))

        battery = []
        for a in course:
            temp = 0
            for b in range(len(a)-1):
                temp += board[a[b]-1][a[b+1]-1]
            battery.append(temp)

        print('#{} {}'.format(case, min(battery)))

cart()

