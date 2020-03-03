import queue
que = queue.Queue()
que.put('kr')
que.put(2)
n = que.get_nowait()
print(n)
print(que.get())
print(que.full())
print(que.empty())

print("end queue\n")


# 우선순위 큐 PriorityQueue
# 내장 모듈 queue에서 PriorityQueue 클래스를 사용하면 간단하게 호출.
from queue import PriorityQueue

pri_que = PriorityQueue()   # 우선순위 큐의 디폴트 사이즈는 무한대.
                            # 최대 크기를 가진 우선순위 큐를 만들때면 maxsize = n 을 사용
# pri_que= PriorityQueue(maxsize = 8)

pri_que.put(4)
pri_que.put(1)
pri_que.put(7)
pri_que.put(3)  # put 메서드로 원소 추가.

print(pri_que.get())

