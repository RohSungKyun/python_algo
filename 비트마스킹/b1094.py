import sys
read = sys.stdin.readline
x = int(read())

nums = [64, 32, 16, 8, 4, 2, 1]
ans=0
for i in nums:
    if x==0:
        break
    if x//i > 0:
        ans+=1
        x %=i
print(ans)