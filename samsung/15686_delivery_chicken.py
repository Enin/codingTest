import itertools, sys, copy
if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 치킨집 탐색
    chicken, home = [], []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i, j])
            elif arr[i][j] == 2:
                chicken.append([i, j])

    print(chicken, home)
    # 치킨집 중에 M개 고르기(조합)
    result = list(itertools.combinations(chicken, M))

    min_distance = float('inf')



    for i in result:
        distance = 0
        for hx, hy in home:
            dist = float('inf')
            for cx, cy in i:
                temp = abs(hx - cx) + abs(hy - cy)
                dist = min(dist, temp)

                #if dist > temp: dist = temp # 거리 최소값으로 업데이트

            distance += dist
        #if min_distance > distance: min_distance = distance
        min_distance = min(min_distance, distance)

    # 출력
    print(min_distance)