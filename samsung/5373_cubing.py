def rotate(c):
    T, X, Y, Z, W = U, L, F, R, B
    if c == 'L':
        T, X, Y, Z, W = L, F, U, B, D
    if c == 'F':
        T, X, Y, Z, W = F, U, L, D, R
    if c == 'R':
        T, X, Y, Z, W = R, D, B, U, F
    if c == 'B':
        T, X, Y, Z, W = B, L, U, R, D
    if c == 'D':
        T, X, Y, Z, W = D, B, R, F, L

    T[0][2], T[1][2], T[2][2], T[2][1], T[2][0], T[1][0], T[0][0], T[0][1] = \
        T[0][0], T[0][1], T[0][2], T[1][2], T[2][2], T[2][1], T[2][0], T[1][0]

    X[2][2], X[2][1], X[2][0], Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2] = \
        Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2], X[2][2], X[2][1], X[2][0]
    #
    # X[0][2], X[1][2], X[2][2], Y[0][0], Y[0][1], Y[0][2], Z[2][0], Z[1][0], Z[0][0], W[2][0], W[2][1], W[2][2] = \
    #     Y[0][0], Y[0][1], Y[0][2], Z[2][0], Z[1][0], Z[0][0], W[2][2], W[2][1], W[2][0], X[2][2], X[1][2], X[0][2]

for _ in range(int(input())):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    n = int(input())
    data = list(input().split())
    for area, dir in data:
        rotate(area)
        if dir == '-':
            rotate(area)
            rotate(area)
    for i in range(3):
        print("".join(j for j in U[i]))
