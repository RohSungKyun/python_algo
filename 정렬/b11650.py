# 좌표 정렬하기 1
import sys
read = sys.stdin.readline
n = int(read())

array = []
for i in range(n):
    a, b = map(int, read().split())
    array.append((a, b))
# 내장 sort함수는 튜플에서 x, y 순으로 ascending으로 정렬해줌
array.sort()
for i in array:
    print(*i)