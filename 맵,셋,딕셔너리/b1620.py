# 파이썬에서 key vlaue로 이루어진 구조는 딕셔너리를 이용하면 된다.
import sys
dict = {}
read = sys.stdin.readline

n, m = map(int, read().split())

for i in range(1, n+1): # 1번 부터 매김
    mon = read().rstrip() # 오른쪽 끝 문자 삭제
    dict[i] = mon
    dict[mon] = i

for i in range(m):
    q = read().rstrip()
    if q.isdigit():
        print(dict[int(q)])
    else:
        print(dict[q])


