# 상어는 1~m 까지의 자연수가 붙어있고 각각이 모두 다르다. 1번 상어는 가장 강력하며 나머지를 쫒아낼 수 있다.
# nxn 격자에 m개 칸에 상어가 한마리씩 들어있고 1초마다 동시에 움직이며 자신의 냄새를 뿌린다.(상하좌우) 냄새는 상어가 k 번 이동하면 사라진다.
# 상어 움직임 조건. 상어는 냄새가 없는 칸을 이동방향으로 잡는다. 만일 없을 경우 자신의 냄새가 있는 칸으로 방향을 잡는다. 이때 가능한 칸이
# 여러개일 수 있으며 이 경우 특정 우선 순위를 따른다.(보고있는 방향에 따라 우선순위는 달라짐) 처음에는 이동 방향이 주어지며 이후에는 이동하는
# 방향이 바라보는 방향이 된다. 한칸에 여러마리의 상어가 남을 경우 가장 작은 번호의 상어를 제외한 나머지를 모두 격자 밖으로 쫒아낸다.
# 1번 상어만 격자에 남아있을 때 까지 몇초 걸리는지 구하여라.
# 필요 함수: 상어 이동, 냄새 업데이트, 상어 탈출, 남아있는 상어 체크
def smelling():  # [상어번호, 냄새] 로 스택킹, [상어 번호, 상어 위치]를 반납
    shark_location = []
    for i in range(n):
        for j in range(n):
            if board_smell[i][j][1] > 0:
                board_smell[i][j][1] -= 1  # 냄새가 0보다 클 경우 1씩 제거해줌.
                if board_smell[i][j][1] == 0:
                    board_smell[i][j][0] = 0

            if board_shark[i][j]:  # 상어 위치를 확인했을 경우
                board_smell[i][j] = [board_shark[i][j][0], k]  # 상어의 번호, 냄새최대치를 추가해줌
                shark_location.append([board_shark[i][j][0], i, j])



    return shark_location


def shark_move(s_num, sx, sy):  # 상어 넘버 + 좌표를 받아와서 해당 상어를 움직인다.
    cd = shark_dir[s_num-1]   # 현재 상어 방향
    # nx, ny = sx + dx[cd], sy + dy[cd]
    # # 격자 이내이고, 방향에 냄새가 없는 경우 이동, 냄새가 있다면 방향전환, 방향전환 해도 없다면 자신의 냄새가 있는 방향으로 이동.
    # if 0 <= nx < n and 0 <= ny < n and board_smell[nx][ny][1] == 0: # 해당방향에 바로 있으면 종료
    #     board_shark[nx][ny].append(s_num)
    #     board_shark[sx][sy].pop()
    #     return

    for d in priority_dir[s_num-1][cd]:    # 상어 번호의 현재 방향에 대한 우선순위 리스트. 빈곳을 찾아서 있다면 이동.
        nx, ny = sx + dx[d], sy + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board_smell[nx][ny][1] == 0:
            board_shark[nx][ny].append(s_num)
            shark_dir[s_num-1] = d
            board_shark[sx][sy].pop()
            return


    for d in priority_dir[s_num-1][cd]:    # 더이상 빈곳이 없을 경우 자신의 냄새가 있는 방향으로 이동
        nx, ny = sx + dx[d], sy + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board_smell[nx][ny][0] == s_num:
            board_shark[nx][ny].append(s_num)
            shark_dir[s_num-1] = d
            board_shark[sx][sy].pop()
            return

    # shark_dir[s_num-1] = cd
    # return [s_num, sx, sy]  # 아무것도 못하면 그냥 종료


def shark_out():    # 남아있는 상어 좌표를 받아온다.
    for i in range(n):
        for j in range(n):
            num = board_shark[i][j]
            if len(num) > 1:
                min_ = min(board_shark[i][j])
                board_shark[i][j] = [min_]




n, m, k = map(int, input().split())
board_temp = [list(map(int, input().split())) for _ in range(n)]   # 0은 빈칸, 숫자는 x번째 상어가 들어간 칸.
board_shark = [[list() for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board_temp[i][j]:
            board_shark[i][j].append(board_temp[i][j])

board_smell = [[[0, 0]]*n for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)   # 상어 방향: 위 아래 왼쪽 오른쪽
shark_dir = list(map(int, input().split()))  # 번호별 상어의 방향    1~4로 주어지므로 0~3으로 변경
for i in range(m):
    shark_dir[i] -= 1

priority_dir = [[list()]*4 for _ in range(m)]    # m개 상어의 각 방향별 우선순위 저장하는 리스트
for i in range(m):  # 각 상어별로 방향별 우선순위
    for c_dir in range(4):  # 4개 방향에 대하여 상어 방향이 위, 아래, 왼쪽, 오른쪽일때 이동 우선순위
        temp_dir = list(map(int, input().split()))
        for d in range(4):
            temp_dir[d] -= 1    # 값 0~3으로 변경

        priority_dir[i][c_dir] = temp_dir


time = 0

while True:
    shark_loc = smelling()  # 남아있는 상어 리스트(번호, 좌표x, 좌표y)

    if len(shark_loc) == 1: # 상어의 수가 1개 이하(1번상어만 남아있을경우)일때
        break

    if time > 1000:
        time = -1
        break

    time += 1   # 시간 1초 증가

    re = len(shark_loc)
    for s in range(re):     # 상어 움직이기.
        s_n, sx, sy = shark_loc.pop()
        shark_move(s_n, sx, sy)

    shark_out()

print(time)
