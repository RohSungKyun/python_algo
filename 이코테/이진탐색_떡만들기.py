# 절단기로 부터 잘려진 떡을 최대로 가져갈 수 있는 절단기 높이를 출력

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
arr = list(map(int, read().split()))

front = 0
rear = max(arr)
result = 0

while front<=rear:
    mid = (front+rear)//2
    total = 0
    for i in arr:
        if i>mid:
            total+= i-mid

    if total<m:
        rear = mid - 1

    else:
        front = mid + 1
        result = mid

print(result)