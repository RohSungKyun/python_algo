import sys
read = sys.stdin.readline
n = int(read())
stack = []

for i in range(n):
    x = list(read().split())
    if x[0]=='push':
        stack.append(x[1])
    elif x[0] =='pop':
        if len(stack)>0:
            tmp=stack.pop()
            print(tmp)
        else:
            print(-1)
    
    elif x[0]=='size':
        print(len(stack))
    elif x[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif x[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])