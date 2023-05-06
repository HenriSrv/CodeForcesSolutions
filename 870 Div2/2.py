from math import gcd


def prime_fact(k):
    c = 2
    res = []
    while k > 1:
        if k % c == 0:
            res += c,
            k = k / c
        else:
            c += 1
    return res


for tt in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    c = abs((arr[0] - arr[-1]))
    if c == 0:
        print(0)
    else:
        for i in range(1, n // 2):
            c2 = abs(arr[i] - arr[-(i + 1)])
            if c2 > c:
                c = c2

        check = [i % c for i in arr]
        fail = False
        for j in range(len(check)):
            if check[j] != check[-(j + 1)] and not fail:
                fail = True
                break
        if not fail:
            print(c)
        else:
            print(0)
