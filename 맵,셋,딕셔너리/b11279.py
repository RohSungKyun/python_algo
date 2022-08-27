import sys, heapq
read = sys.stdin.readline
n = int(read())
heap=[]
for i in range(n):
    x = int(read())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, [-x, x]) # 음수에서는 상수가 커질수록 더욱 작은 값이 되어 버리기 때문에 힙에 넣을때 -n값을 넣게 된다면 반대의 형태로 구현 가능
