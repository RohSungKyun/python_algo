
import sys

read = sys.stdin.readline
n, k = map(int, read().split())
arr1 = list(map(int, read().split()))
arr2 = list(map(int, read().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse=True)

tmp = []
for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break
ans=0
for i in arr1:
    ans+=i
print(ans)