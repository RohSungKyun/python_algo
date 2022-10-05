import sys
read = sys.stdin.readline

for i in range(int(read())):
    k = int(read())
    n = int(read())
    floor = [i for i in range(n+1)]

    for _ in range(k):
        for i in range(1, n+1):
            floor[i] += floor[i-1]
    print(floor[-1])