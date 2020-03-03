## 달리기 문제
# 우선순위 큐 사용
import queue

# N = int(input())
# S = [0]
# R = [0]
# for i in range(N):
#     s = int(input())
#     print("받은s", s)
#     if i == 0:
#         S.insert(i, s)
#         R.insert(i, 1)
#         print("i==0 동작 r출력", R)
#     else:
#
#         for j in range(i+1):
#             if s > S[j]:
#                 S.insert(j, s)
#                 print("break 수행 s 삽입", S)
#                 break
#             else:
#                 print("넘어감")
#                 continue
#             print("맨 마지막 삽입", S)
#             S.insert(-2, s)
#         R.insert(i, S.index(s)+1)
#         print("r 출력1", R)
#
# print("2s", S)
# print("2r", R)




N = int(input())
S = [0]
R = [0]
for i in range(N):
    s = int(input())
    if i == 0:
        S.insert(i, s)
        R.insert(i, 1)

    else:

        for j in range(i+1):
            if s > S[j]:
                S.insert(j, s)
                break
            else:
                continue
            S.insert(-2, s)
        R.insert(i, S.index(s)+1)

for i in range(N):
    print(R[i])

# 좌표 압축 + 세크먼트 트리 알고리즘
# 1. 좌표 압축 수행.
# 전체 능력치 값은 10억까지 입력되지만 최대 들어올 수 있는 N은 3~ 50만개 이므로 좌표 압축을 사용하면 값을 줄일 수 있다.
# 세그먼트 트리 사용.
# 세그먼트 트리(구간트리)는 구간 합을 더 쉽게 만들어주는 쿼리 방법이다.
# 리프 노드에는 최초 받아온 데이터가 들어가며 각 자식노드의 부모노드는 자식노드의 합을 데이터로 갖는다.
# 세그먼트 트리는 트리배열과 어레이베열 2개가 있으며, 트리배열은 세그먼트 트리를 만드는 배열이고 arr배열은 처음 입력받아 생성한 배열이다.
