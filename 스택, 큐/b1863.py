# 스카이라인 쉬운거
import sys
read = sys.stdin.readline
n = int(read())
stack = []
cnt=0
stack.append(0)

# stack을 사용해야 하는 이유: 건물의 높이가 낮아지는 경우를 고려해야하기 때문이다.
for i in range(n):
    x, y = map(int, read().split())
    if y > stack[-1]: # 건물의 높이가 높아지면 cnt+=1
        stack.append(y)
        cnt+=1
    else: # 건물의 높이가 낮아지는 경우
        while stack and stack[-1]>y:
            stack.pop()
        if stack[-1]<y:
            stack.append(y)
            cnt+=1
            


print(cnt)
