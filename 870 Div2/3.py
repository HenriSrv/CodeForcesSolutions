


def modi(p, k, memo={}):
    if k <= 1:
        return "YES"
    elif p % k == 0:
        return "NO"
    elif (p, k) in memo:
        return memo[(p, k)]
    else:
        result = modi(p, k - p % k, memo)
        memo[(p, k)] = result
        return result


for tt in range(int(input())):
    n, m = map(int, input().split())
    if n % m == 0:
        print("NO")
    else:
        for i in range(n):
            print(modi(n, m))




