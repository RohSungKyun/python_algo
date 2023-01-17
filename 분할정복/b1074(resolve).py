import sys
read = sys.stdin.readline
n, r , c = list(map(int, read().split()))

def getIndex(size, x, y):
    global index
    if x==r and y == c:
        print(index)
        sys.exit(0)

    if size == 1:
        index+=1
        return
        
    if not (x<=r<x+size and y<=c<y+size):
        index+=size**2
        return
    
    nbs = size//2
    getIndex(nbs, x, y) # 제 1 사분면
    getIndex(nbs, x, y+nbs) # 2 사분면
    getIndex(nbs, x+nbs, y) # 3 사분면
    getIndex(nbs, x+nbs, y+nbs) # 4 사분면

index = 0
getIndex(2**n, 0, 0)
