import sys
read = sys.stdin.readline
n = int(read())
# 2원 5원 동전을 작은 개수로 분배 => 5로 나눈 나머지가 1, 3인 경우 따로 처리

if n==1 or n==3:
    print(-1)

elif n%5==3:
    print(((n//5)-1)+4)
elif n%5==1:
    print(((n//5)-1)+3)
else:
    print((n//5)+(n%5)//2)

