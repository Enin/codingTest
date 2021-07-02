#  다리를 지나는 트럭
#
# 문제 설명
#
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. -- 모든 트럭이 건너는 최소시간
#  다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, -- 트럭은 순서대로 들어간다.
#  다리는 weight 이하까지의 무게를 견딜 수 있습니다.
#  단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다. -- 다리가 버틸 수 있는 하중 만큼 다리위에 트럭이 올라갈 수 있다.
#
# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
#  무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
# 경과 시간 	다리를 지난 트럭 	다리를 건너는 트럭 	대기 트럭
# 0 	    [] 	            [] 	                [7,4,5,6]
# 1~2 	    [] 	            [7] 	            [4,5,6]
# 3 	    [7] 	        [4]             	[5,6]
# 4 	    [7] 	        [4,5] 	            [6]
# 5 	    [7,4] 	        [5] 	            [6]
# 6~7 	    [7,4,5] 	    [6] 	            []
# 8 	    [7,4,5,6] 	    [] 	                []
#
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.
#
# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length,
#  다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.
#  이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
# 제한 조건
#
#     bridge_length는 1 이상 10,000 이하입니다.
#     weight는 1 이상 10,000 이하입니다.
#     truck_weights의 길이는 1 이상 10,000 이하입니다.
#     모든 트럭의 무게는 1 이상 weight 이하입니다.
from collections import deque


def solution(bridge_length, weight, truck_weights): # 다리 길이(한번에 올라갈수있는 다리 길이
    answer = 0  # 지난 시간.
    q_truck = deque(truck_weights)
    q_bridge = deque([0]*bridge_length, maxlen=bridge_length)
    bridge_weight_now = 0

    while q_bridge:    # 큐에 들어있는 트럭 수가 없어질때까지 수행.
        answer += 1
        t_out = q_bridge.popleft()
        bridge_weight_now -= t_out
        if q_truck:
            if weight - bridge_weight_now >= q_truck[0]: # 남은 여유 무게가 첫벗째 트럭무게보다 클경우
                t_now = q_truck.popleft()
                q_bridge.append(t_now)
                bridge_weight_now += t_now
            else:
                q_bridge.append(0)

    return answer


i_bridge_length, i_weight, i_truck_weights = 100, 	100, 	 	[10,10,10,10,10,10,10,10,10,10]

print(solution(i_bridge_length, i_weight, i_truck_weights))
