import sys
read = sys.stdin.readline
# input 값은 2^n * 2^n에서 n, 행, 열을 받아옴
n, r, c = map(int, read().split())

def getIndex(mapsize, x, y):
    index=0
    

