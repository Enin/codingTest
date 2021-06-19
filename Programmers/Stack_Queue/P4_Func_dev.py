# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
#
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
#
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
# 제한 사항
#
#     작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
#     작업 진도는 100 미만의 자연수입니다.
#     작업 속도는 100 이하의 자연수입니다.
#     배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
from collections import deque


def solution(progresses, speeds):
    answer = []

    while progresses:
        q = deque(progresses)
        cnt = 0
        while q:
            check = q.popleft()
            if check >= 100:
                cnt += 1
            else:
                break
        if cnt > 0:
            answer.append(cnt)
            progresses = progresses[cnt:]
            speeds = speeds[cnt:]

        if not progresses:
            break
        else:
            for i in range(len(progresses)):
                progresses[i] = progresses[i] + speeds[i]

    return answer


i_progresses = [95, 90, 99, 99, 80, 99]
i_speeds = [1, 1, 1, 1, 1, 1]



def best_solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # 초기 상태 또는 Q의 마지막의 횟수값이 수행횟수보다 작을 경우
            Q.append([-((p-100)//s),1])     # speed가 몇번 수행되야 하는지 [횟수, cnt=1] 로 작성
        else:
            Q[-1][1]+=1 # 위 조건이 아닐경우는 Q의 마지막의 cnt를 1개 증가

    return [q[1] for q in Q]    # 마지막에 각 cnt 부분만 빼내서 리스트로 출력

print(best_solution(i_progresses, i_speeds))