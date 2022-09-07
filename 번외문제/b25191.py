import sys
read = sys.stdin.readline

n = int(read())
# 콜라 2개 맥주 1개
c, b = map(int, read().split())

max_chicken = (c//2)+b

if max_chicken>n:
    print(n)
else:
    print(max_chicken)


