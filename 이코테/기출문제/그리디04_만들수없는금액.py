import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
nums.sort()

# 금액을 1부터 시작해서 만들 수 있는지 판단.
ans = 1

for i in nums:
    if ans < i: # 금액이 보유한 화폐단위 보다 작으면 
        break
    ans+=i

print(ans)