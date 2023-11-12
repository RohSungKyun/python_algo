# 연산자를 끼워넣어 만들수 있는 최대값, 최소값을 구하기
# 주어진 수의 순서를 바꿔도 안된다.
# 연산 우선순위 적용x

import sys
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))
operator = list(map(int, read().split()))

max_val = -1e9
min_val = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global max_val, min_val
    
    if depth == n:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return
    
    if plus:
        dfs(depth+1, total+nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*nums[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/nums[depth]), plus, minus, multiply, divide-1)

dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])

print(max_val)
print(min_val)