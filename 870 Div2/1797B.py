for tt in range(int(input())):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    rev_grid = grid.copy()
    for i in range(1, n // 2 + 1):
        rev_grid[-i] = grid[-i][::-1]

    c = 0

    for j in range(0, n // 2):
        for i in range(n):
            if rev_grid[j][i] != rev_grid[-(j + 1)][i]:
                c += 1

    if n % 2 != 0:
        y = n // 2
        for x in range(n):
            if rev_grid[y][x] != grid[y][x]:
                c += 1

    if c <= k and ((n % 2 == 0 and (c - k) % 2 == 0) or n % 2 != 0):
        print("YES")
    else:
        print("NO")

# SO CLOSE IDK WHY IT DONT WORK