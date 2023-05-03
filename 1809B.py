import math
from decimal import *

for t in range(int(input())):
    n = int(input())
    if n < 2:
        print(0)
    else:
        getcontext().prec = 80
        print(math.floor(Decimal(n-1).sqrt()))

