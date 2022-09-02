import sys
read = sys.stdin.readline
# 중요한 조건: 모두 사용할 필요는 없다.
n = int(read())
rope = []

for i in range(n):
    rope.append(int(read()))
rope = sorted(rope)[::-1] # 내림차순 정렬

mv=0

for i in range(n):
    tmp = rope[i]*(i+1)
    mv = max(tmp, mv)

print(mv)