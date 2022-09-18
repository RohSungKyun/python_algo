import sys
read = sys.stdin.readline

n = int(read())
n_list = list(map(int, read().split()))

m = int(read())
m_list = list(map(int, read().split()))

n_list.sort()

for i in range(m):
    start = 0 # 인덱스
    end = n-1
    while start<=end:
        mid = (start+end)//2
        if m_list[i]==n_list[mid]:
            m_list[i] = 1
            break
        elif m_list[i] < n_list[mid]:
            end = mid-1
        else:
            start=mid+1

for i in range(m):
    if m_list[i]!=1:
        m_list[i]=0

for i in m_list:
    print(i, end=" ")
