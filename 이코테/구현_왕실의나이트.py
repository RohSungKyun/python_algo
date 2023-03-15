# 8x8 체스판 
# 수평으로 두칸 + 수직으로 한칸, 수직으로 두칸, 수평으로 한 칸
#  나이트가 이동할 수 있는 경우의 수를 출력 행 열은 각각 1~8, a~h
# hint : 나이트가 이동할 수 있는 경우의 수를 모두 배열에 저장하기

import sys
read = sys.stdin.readline

roc = read()
row = int(roc[1])
col = int(ord(roc[0])) - int(ord('a')) + 1
method = [(-2, -1), (-1, -2), (2, -1), (-1, 2), (-2, 1), (1, -2), (1, 2), (2, 1)] # 8가지

cnt = 0 
for move in method:
    newrow = row + move[0]
    newcol = col + move[1]
    if newrow <= 8 and newrow >= 1 and newcol >= 1 and newcol <= 8:
        cnt+=1

print(cnt)