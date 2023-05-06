for tt in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    sv = min(li)
    c = 0

    for i in li:
        if i > sv:
            c += 1

    if n-c <= 0:
        print(-1)

    elif sv >= n:
        print(-1)

    elif c < sv:
        print(-1)

    else:
        print(c)
