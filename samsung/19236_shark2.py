# 현재물고기, 다음물고기
# 물고기는 번호 순서대로 이동
# 이동할 수 없는칸은 상어가 있거나 공간의 경계를 넘을때.
# 이동할 수 없다면 이동할 수 있는 칸이 나올때 까지 반시계방향으로 방향을 변경.
# 이동할때는 이동할 칸의 물고기와 자리를 변경.
# 상어는 0,0 에서 시작. 상어의 방향은 0,0 의 물고기 방향과 같다. 물고기가 모두 움직인 다음 상어가 움직인다.
# 상어는 방향에 있는 칸으로 이동하며 한번에 여러개 칸을 이동 가능하다. 물고기가 없는 칸으로는 이동할 수 없다.
# 상어가 물고기가 있는 칸으로 이동할 시에는 그 칸의 물고기를 먹고 그 물고기의 방향을 가지게 된다.
# 이동중에 지나가는 칸에 있는 물고기는 먹지 않는다. 이동할 수 있는 칸이 없으면 집으로 돌아간다.
# 상어가 먹을 수 있는 물고기 번호의 합의 최대 값을 구하여라.
# 1. 물고기 이동 함수
# 2. 상어가 물고기를 먹는 경우의 수 - bfs
import copy


def shark_move(arr, sx, sy):
    candi = []  # 상어가 갈수있는 위치 저장
    d = arr[sx][sy][1]
    for _ in range(1, 4):
        nx, ny = sx + dx[d], sy + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= arr[nx][ny][0] <= 16:
            candi.append([nx, ny])
        sx, sy = nx, ny

    return candi


def fish_find(arr, num): # num번째 물고기를 탐색하여 좌표를 리턴
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == num:
                return (i, j)
    return None


def fish_move(arr, sx, sy):
    for num in range(1, 17):
        pos = fish_find(arr, num)
        if pos is None:
            continue
        x, y = pos[0], pos[1]
        d = arr[x][y][1]
        for _ in range(8):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == sx and ny == sy):
                    arr[x][y][0], arr[nx][ny][0] = arr[nx][ny][0], arr[x][y][0]
                    arr[x][y][1], arr[nx][ny][1] = arr[nx][ny][1], d
                    break
            d = (d + 1) % 8


def dfs(arr, sx, sy, point):  # 재귀함수. 상어의 현재 좌표 및 포인트를 입력받아서 수행. 상어 먹기-> 물고기 이동 -> 상어 이동가능한 위치 탐색
    global max_ans
    arr = copy.deepcopy(arr)
    c_fish = arr[sx][sy][0]
    arr[sx][sy][0] = -1    # 현 좌표를 상어가 먹은것 처리.
    fish_move(arr, sx, sy)       # 생선 움직기기
    shark_next = shark_move(arr, sx, sy)

    max_ans = max(max_ans, point + c_fish)

    for nx, ny in shark_next:
        dfs(arr, nx, ny, point + c_fish)


board = [[0]*4 for _ in range(4)]
dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1) # 북 북서 서 남서 남 남동 동 동북
max_ans = 0
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [temp[j*2], temp[(j*2)+1]-1]  # board[i][j][0] = 물고기번호, board[i][j][1] = 물고기 방향

dfs(board, 0, 0, 0)

print(max_ans)