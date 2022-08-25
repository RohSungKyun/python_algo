import sys
# 행동의 최소 횟수
# 단지 수 세기와 비슷한 문제

read = sys.stdin.readline
str = read()

cnt=0
for i in range(len(str)-1):
    if str[i]!=str[i-1]:
        cnt+=1

print(cnt//2)

