# 탐욕 알고리즘 - 컨테이너 운반
#
# 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
#
# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
#
# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.
#
# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.
#
# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

def containers():
    T = int(input())

    for case in range(1, T+1):
        N, M = map(int, input().split())
        cargo_W = list(map(int, input().split()))
        truk_T = list(map(int, input().split()))
        max_w = 0

        for t in truk_T:
            tmp = 0
            for w in cargo_W:
                if tmp < w <= t:
                    tmp = w

            if tmp == 0:
                continue
            else:
                max_w += tmp
                cargo_W.remove(tmp)

        print('#{} {}'.format(case, max_w))



# 탐욕 알고리즘 - 화물 도크
#
# 24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.
#
# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.
#
# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있고, 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
#
# 예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능하다.

def container_dock():
    
