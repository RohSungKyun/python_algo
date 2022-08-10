# n-queen문제
# n x n 크기의 체스판에 퀸 n개가 주어졌을 경우 서로 공격할 수 없는 위치에 놓는 문제 => 배치하는 방법의 수를 출력
n = int(input())

# 여기서 dfs(x) x번째 줄에 퀸을 놓는 경우의 수
# 같은 행/열에 퀸이 2개 이상 있어서 안 되고, 같은 대각선에도 퀸이 2개 이상 존재하면 안 된다.
count=0
arr=[0]*(n+1)
ver=[False]*(n+1) # 가로 배열
diag1=[False]*2*(n+1) # 대각선1 배열
diag2=[False]*2*(n+1) # 대각선2 배열
def dfs(x):
    global count, arr, ver, diag1, diag2
    if x == n+1:
        count+=1
        return
    
    for i in range(1, n+1):
        check=True
        if ver[i] or diag1[x+i] or diag2[x-i+n]: # 서로 공격할 수 있는지 판단
            continue
        ver[i] = diag1[x+i] = diag2[x-i+n] =True
        dfs(x+1)
        ver[i] = diag1[x+i] = diag2[x-i+n] =False

dfs(1)
print(count)