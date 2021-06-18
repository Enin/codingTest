# 컨베이어벨트
from collections import deque
from itertools import chain
from collections import Counter

# 0번위치 : 올라가는 위치, n-1번위치 내려가는위치
# 올라가는 위치에서만 땅에서 벨트로 올라가고 내려가는 위치에서는 반드시 땅으로 내려가야됨.
# 로봇이 어떤 칸에 올라가거나 이동하면 그 칸의 내구도는 즉시 1만큼 감소. - 내구도가 0인 칸에는 로봇이 올라갈 수 없음. 이때 내구도는 ai
# 벨트를 이용해 로봇을 건너편으로 이동시킨다. 로봇움직이는 순서
# 1. 벨트가 1칸 회전
# 2. 가장먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 1칸 이동. 이동할 수 없다면 그대로.
#   이동하려는 칸에는 로봇이 없어야하며 그 칸의 내구도가 1 이상 남아있어야함.
# 3. 올라가는 위치에 로봇이 없다면 로봇을 1개 올림.
# 내구도 0인 칸의 개수가 k개 이상일때 과정을 종료. 그렇지 않으면 1번으로 돌아감.
# 종료 일때 몇번째 단계가 진행되는지 구할것

n, k = map(int, input().split())
belt = list(map(int, input().split()))  # 2n 개 줄 1~n까지 윗줄 > n+1~2n까지 아래줄. 각 값은 칸의 내구도.
level = 0   # 단계를 나타냄
robot = [0]*n   # 로봇의 위치. 로봇 위치는 1~n까지만 있으며 n에서


def belt_rotate():  # 1번    벨트만 움직임
    last = belt[-1]
    for i in range(2*n-1, 0, -1):
        belt[i] = belt[i-1]
    belt[0] = last
    for i in range(n-1, 0, -1):
        robot[i] = robot[i-1]
    robot[0] = 0


def robot_move():
    for i in range(n-1, -1, -1):
        if i == n-1:
            robot[i] = 0
        else:
            if robot[i] and robot[i+1] == 0:    # i번째 로봇이 있고 다음칸에 로봇이 없을경우 다음 칸의 내구도를 확인
                if belt[i+1] > 0:   # 내구도가 0보다 클경우 로봇의 위치를 1칸 옮기고 해당 위치의 내구도를 1 감소
                    robot[i+1] = 1
                    robot[i] = 0
                    belt[i+1] -= 1


def add_robot():
    if belt[0] > 0 and robot[0] != 1:
        robot[0] = 1
        belt[0] -= 1


def k_check():  # 벨트의 0 개수 세서 리턴
    h = Counter(belt)
    return h[0]


while True:
    level += 1
    belt_rotate()
    robot_move()
    add_robot()
    zero_num = k_check()

    if zero_num >= k:
        break

print(level)



