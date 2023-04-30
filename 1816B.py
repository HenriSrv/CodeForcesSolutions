# problem description found at: https://codeforces.com/problemset/problem/1816/B

n_tests = int(input())
while n_tests > 0:
    n = int(input())

    grid = [[0 for i in range(n)] for j in range(2)]  # establish our grid
    odds = [i for i in range(1, 2 * n + 1, 2)]
    front_odd = 0
    evens = [i for i in range(2, 2 * n + 1, 2)]
    front_even = 0

    grid[1][-1] = odds.pop(-1)

    for i in range(n):
        if i % 2 == 0:
            grid[0][i] = evens.pop(-1)  # pop(-1) is constant, .pop(0) is slow hence the pointers
        else:
            grid[0][i] = evens[front_even]
            front_even += 1

    for i in range(n - 1):
        if i % 2 == 0:
            grid[1][i] = odds[front_odd]
            front_odd += 1
        else:
            grid[1][i] = odds.pop(-1)

    # formats result
    res_1 = ' '.join([str(i) for i in grid[0]])
    res_2 = ' '.join([str(i) for i in grid[1]])
    print(f"{res_1}\n{res_2}")
    n_tests -= 1

# success
