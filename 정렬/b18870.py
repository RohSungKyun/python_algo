# 좌표 압축 : 여러 곳에 흩뿌려진 좌표들을 연속된 수들로 모아 압축하는 것이다. 입력은 적은데 범위는 넓은 경우 인덱스를 부여하는 방식
import sys
read = sys.stdin.readline

n = int(read())
number = list(map(int, read().split()))

# 집합으로 중복을 제거한 인덱스를 만들어 낸다.
numlist = list(set(number))
tmp = sorted(numlist)

# 집합을 이용하여 좌표압축을 진행한다.
rank = {}
for i in range(len(tmp)):
    rank[tmp[i]] = i

for i in number:
    print(rank[i], end=' ')