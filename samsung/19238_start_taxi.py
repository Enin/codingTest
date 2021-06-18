# 손님을ㄷ ㅗ착지로 데려다줄때 연료가 충전되고, 연료가 바닥나면 그날 업무가 끝난다.
# 택시기사는 m 명의 승객을 태우는 것이 목표다. 격자 nxn에 각 칸은 비어있거나 벽이 세워있다.
# 택시는 인접한칸중 빈칸으로만 이동가능. 특정위치로 이동할때 항상 최단경로로 이동(bfs)
# m명의 승객이 빈칸에 서있고 다른칸으로 이동하려한다. 한번에 한명의 승객만 탑승.(m 번 반복)
# 승객은 움직이지 않고 출발지에서만 택시를 타고 목적지에서만 내릴 수 있음.
# 현위치에서 가장 짧은 최단거리 고객을 고름.(여러명일 경우 행번호가 가장 작고, 열번호가 가장 작은 승객을고름)
# 같은 위치일때 최단거리 0
# 성공적으로 이동시키면 소모한 연료 양의 2배 충전
# 이동시킨 동시에 연료가 바닥날 경우에는 실패로 간주안함
# 연료가 바닥나면 업무종료
# 모두 태울수잇는지 확인하고 가능할 경우 최종 연료 양을 출력
from collections import deque

n, m, tank = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] # 0 빈칸 1 벽
taxi_x, taxi_y = map(int, input().split())  # 택쉬 좌표
taxi_x -= 1
taxi_y -= 1
passengers = []
goals = []
for i in range(m):
    px, py, gx, gy = map(int, input().split()) # m번째 승객의 좌표 [승객행, 승객열, 목적지행, 목적지열]
    passengers.append([px-1, py-1])
    goals.append([gx-1, gy-1])  # 승객별 도착지

dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)


def bfs_pas(tx, ty):
    global tank
    passenger = []
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append([tx, ty, 0])   # 좌표, 거리
    while q:
        x, y, distance = q.popleft()
        if distance > tank:
            return None
        visited[x][y] = True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and not visited[nx][ny]:
                if [nx, ny] in passengers:
                    passenger.append([nx, ny, passengers.index([nx, ny]), distance+1])    # 좌표, 번호, 거리

                q.append([nx, ny, distance+1])

    passenger = sorted(passenger, key= lambda x: (x[3], x[0], x[1]))
    return passenger # 가장 우선순위 높은 순으로 리턴


def goal_bfs(tx, ty, gx, gy):
    global tank
    q = deque()
    visited = [[False]*n for _ in range(n)]
    q.append([tx, ty, 0])
    while q:
        x, y, distance = q.popleft()
        if distance > tank:
            return -1
        visited[x][y] = True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and not visited[nx][ny]:

                if nx == gx and ny == gy:
                    return distance+1

                q.append([nx, ny, distance+1])


for _ in range(m):
    temp = bfs_pas(taxi_x, taxi_y)   # 좌표, 승객번호, 거리
    if not temp:
        tank = -1
        break
    pas_x, pas_y, pas_num, pas_dist = temp[0]
    tank -= pas_dist

    goal_dist = goal_bfs(pas_x, pas_y, goals[pas_num][0], goals[pas_num][1])
    if goal_dist == -1:
        tank = -1
        break
    else:
        tank += goal_dist
    taxi_x, taxi_y = goals[pas_num][0], goals[pas_num][1]
    passengers.pop(pas_num)
    goals.pop(pas_num)

print(tank)