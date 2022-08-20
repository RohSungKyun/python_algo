import sys
read = sys.stdin.readline
arr = read().split('-') # -를 기준으로 묶는다
# 이후 -뒤에 오는 모든 수를 묶어주면 된다.

ans =[]


for i in arr:
    x=0
    tmp=i.split('+')
    for j in tmp:
        x+=int(j)
        
    ans.append(x)

target=ans[0]

for i in range(1, len(ans)):
    target-=ans[i]
print(target)