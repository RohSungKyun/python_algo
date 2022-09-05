import sys
read = sys.stdin.readline
# 닫는 괄호는? 빼준다. 레이저를 만나면 카운트
arr = list(read().rstrip())
stack = []
cnt=0

for i in range(len(arr)):
    if arr[i] == '(': # 여는 괄호일 경우
        stack.append(i)
    
    else:
        if arr[i-1]=='(': # 레이저인 경우
            stack.pop()
            cnt = cnt + len(stack)
        
        else:
            stack.pop()
            cnt+=1
            

print(cnt)