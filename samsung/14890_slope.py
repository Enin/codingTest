def road(arr):
    global ans
    for i in range(N):
        pre = arr[i][0]
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == pre:
                cnt += 1
                pre = arr[i][j]
            elif arr[i][j] == pre + 1 and cnt >= 0:
                if cnt >= L:
                    cnt = 1
                    pre = arr[i][j]
                else:
                    break
            elif arr[i][j] == pre - 1 and cnt >= 0:
                cnt = - L + 1
                pre = arr[i][j]
            else:
                break
        else:
            if cnt >= 0:
                ans += 1

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

arr_t = [list(x) for x in zip(*arr)]



road(arr)
road(arr_t)


print(ans)
