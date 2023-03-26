# 내림차순 정렬
import sys
read = sys.stdin.readline

n = int(read())
arr = []

for i in range(n):
    arr.append(int(read()))

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=' ')