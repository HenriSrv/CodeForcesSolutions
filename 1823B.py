# problem description found at: https://codeforces.com/problemset/problem/1823/B

n_tests = int(input())


def solve(n, k, arr):
    target = sorted(arr, reverse=False)
    if arr == target:  # if list already sorted, return 0 immediately
        return 0

    for j in range(n):  # compare each i and (i + k)th element to see if they can be swapped
        for i in range(n-k):
            if arr[i] > arr[i + k]:
                arr[i], arr[i + k] = arr[i + k], arr[i]

    if arr == target:
        return 0

    count = 0
    while count <= 2:
        for i in range(n):
            if arr[i] != target[i]:
                count += 1
        if count <= 2:  # if this is true, then exactly two elements are misplaced .'. only 1 pre-swap is required
            return 1
    return -1


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    tempP = p.copy()
    result = solve(n, k, tempP)
    if result != -1:
        return result
    else:
        for i in range(n):
            for j in range(n):
                temp = p.copy()
                temp[i], temp[j] = temp[j], temp[i]
                result = solve(n, k, temp)
                if result == 0:
                    return 1
        return -1


while n_tests > 0:
    print(main())
    n_tests -= 1
