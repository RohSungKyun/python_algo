# ATM 제일 짧은 시간이 걸리는 사람을 앞에 위치시키면 되는 문제이다.
import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))
arr.sort()
tmp=[]
ans=0

for i in range(n):
    tmp.append(i)
    ans += arr[i] *(n-i) # => 여기서 n-1은 해당 문자가 반복해서 더해지는 횟수를 한번에 곱하는 것이다. O(n)

print(ans)
