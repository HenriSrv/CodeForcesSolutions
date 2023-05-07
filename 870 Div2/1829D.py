def solve(n, m):
    if n == m:
        return(1)

    if n % 3 != 0 or m > n:
        return(0)

    return solve(n//3, m) or solve(n-(n//3), m)

for tt in range(int(input())):
    n, m = map(int, input().split())
    if solve(n, m):
        print("YES")
    else:
        print("NO")


