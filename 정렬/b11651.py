# 좌표 정렬하기 2
import sys
read = sys.stdin.readline
n = int(read())

array = []
for i in range(n):
    a, b = map(int, read().split())
    array.append((a, b))

# sort함수에 람다를 이용하여 원하는 기준으로 정렬한다. 
# key는 함수 또는 람다에 따라 정렬
array.sort(key = lambda x : (x[1], x[0]))
for i in array:
    print(*i)