# 투 포인터를 활용하여 반복문의 사용을 줄임
import sys
read = sys.stdin.readline
n, d, k, c = map(int, read().split())

arr = [int(read().rstrip()) for _ in range(n)]
lp, rp = 0, 0
ans = 0

while lp != n:
    rp = lp + k
    tmp = set()
    coupon = False
    for i in range(lp, rp):
        i%=n
        tmp.add(arr[i])
        if arr[i] == c:
            coupon = True
    cnt=0
    if coupon:
        cnt = len(tmp)
    else:
        cnt = len(tmp)+1

    if cnt>ans:
        ans = cnt
    lp+=1
    
print(ans)