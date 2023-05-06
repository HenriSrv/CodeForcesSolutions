def modi(p, k, memo={}):
    while k > 1:
        if p % k == 0:
            return "NO"
        elif (p, k) in memo:
            return memo[(p, k)]
        else:
            memo[(p, k)] = 1
            k = k - p % k
    return "YES"

for tt in range(int(input())):
    n, m = map(int, input().split())
    if n % m == 0:
        print("NO")
    else:
        print(modi(n, m))
