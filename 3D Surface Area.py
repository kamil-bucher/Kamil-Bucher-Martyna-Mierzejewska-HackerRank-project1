H, W = map(int, input().split())

A = []
for i in range(H):
    A.append(list(map(int, input().split())))

surface = H * W * 2

for i in range(H):
    for j in range(W):
        h = A[i][j]

        if i == 0:
            surface += h
        else:
            if h > A[i-1][j]:
                surface += h - A[i-1][j]

        if i == H-1:
            surface += h
        else:
            if h > A[i + 1][j]:
                surface += h - A[i + 1][j]

            if j == 0:
                surface += h
            else:
                if h > A[i][j - 1]:
                    surface += h - A[i][j - 1]

            if j == W - 1:
                surface += h
            else:
                if h > A[i][j + 1]:
                    surface += h - A[i][j + 1]

            print(surface)