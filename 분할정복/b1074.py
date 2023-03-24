# 분할정복 : 분할한 문제들이 서로 영향을 미침 vs 동적 계획법 : 분할한 문제들이 서로 영향을 미치지 않음
# 분할정복의 과정 1. 분할, 2. 정복, 3. 조합
import sys
read = sys.stdin.readline
# input 값은 2^n * 2^n에서 n, 행, 열을 받아옴
n, r, c = map(int, read().split())

def getIndex(mapsize, x, y):
    global index

    if x == r and y == c: # 값을 찾아냈을 경우
        print(index)
        sys.exit(0)
    
    if mapsize == 1: # 분할하여 1이 될 경우
        index+=1
        return
    
    if not (x <= r < x+mapsize and y <= c < y+mapsize): # 분할한 범위에 값이 없을 경우
        index+=mapsize**2 # 인덱스를 더해줌
        return 
    
    # z방향으로 재귀 사분면 탐색 (4등분)
    nbs = mapsize//2 
    getIndex(nbs, x, y) # 1 사분면
    getIndex(nbs, x, y+nbs) # 2 사분면
    getIndex(nbs, x+nbs, y) # 3 사분면
    getIndex(nbs, x+nbs, y+nbs) # 4 사분면

index=0
getIndex(2**n, 0, 0)

    

