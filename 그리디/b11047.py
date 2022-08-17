import sys
read = sys.stdin.readline

n, k = map(int, read().split())
arr = []
for i in range(1, n+1):
    arr.append(int(read())) # 동전의 종류를 순서대로 저장(오름차순으로 저장됨)

arr.sort(reverse=True) # 내림차순(큰 금액부터 탐색)

cnt = 0

for i in range(len(arr)): # 큰 금액부터 탐색
    if (arr[i]>k): # k보다 커지는 경우
        continue
    else: # 처음으로 k보다 작아질때
        cnt += k//arr[i]
        k%=arr[i]
        
print(cnt)

