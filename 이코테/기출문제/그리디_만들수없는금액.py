# 조합해서 만들수 없는 금액의 최솟값

import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
nums.sort()
ans = 1

for i in nums: #  3 2 1 1 9 => 4
    if ans<i:
        break
    ans+=i

print(ans)