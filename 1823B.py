# problem description found at: https://codeforces.com/problemset/problem/1823/B

n_tests = int(input())


def solve(n, k, p):
    target = sorted(p, reverse=False)
    if p == target:  # if list already sorted, return 0 immediately
        return 0

    for j in range(n):  # compare each i and (i + k)th element to see if they can be swapped
        for i in range(n-k):
            if p[i] > p[i + k]:
                p[i], p[i + k] = p[i + k], p[i]

    if p == target:
        return 0

    count = 0
    while count <= 2:
        for i in range(n):
            if p[i] != target[i]:
                count += 1
        if count <= 2:  # if this is true, then exactly two elements are misplaced .'. only 1 pre-swap is required
            return 1
    return -1
# currently fails when 1 swap would allow the remaining swaps to occur properly. eg 4 2: 3 1 4 2
# if you swapped the 1 and 4 you would have 3 4 1 2, which can then be sorted with the step k (2)


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    return solve(n, k, p)


while n_tests > 0:
    print(main())
    n_tests -= 1
