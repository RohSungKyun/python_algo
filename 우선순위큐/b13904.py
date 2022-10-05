import sys, heapq
read = sys.stdin.readline

n = int(read())
ans = [0]*1001
heap = []

for i in range(n):
    day, score = map(int, read().split())
    heapq.heappush(heap, [-score, day, score]) # 마감일이 큰 순서, 점수가 큰 순서대로 정렬된다.

while heap: # 우선 마감일이 긴 순서부터 점수가 큰 경우를 채택한다.
    tmp = heapq.heappop(heap)
    for i in range(tmp[1], 0, -1): # 기간의 마지막 날 부터 접근한다.
        if ans[i]==0:
            ans[i]=tmp[2] # 저장이 끝났으면 break를 만나서 반복문을 나간다.
            break
        
print(sum(ans))