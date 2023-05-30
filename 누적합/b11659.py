import sys
read = sys.stdin.readline

n, m = map(int, read().split()) # the number of numbers, the number of frequent occurrences
arr = list(map(int, read().split()))

prefix_sum = [0] # init prefix sum array // add to 0 in index to align index
tmp = 0 
for i in arr:
    tmp += i
    prefix_sum.append(tmp)

for j in range(m):
    a, b = map(int, read().split()) # range
    print(prefix_sum[b] - prefix_sum[a-1])
