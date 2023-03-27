import sys
read = sys.stdin.readline

n = int(read())
arr1 = list(map(int, read().split()))
arr1 = sorted(arr1)

m = int(read())
arr2 = list(map(int, read().split()))

def b_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] > target: # 찾는 값이 중앙값보다 작을 경우
            end = mid - 1
        elif array[mid] == target:
            return target
        else: # 찾는 값이 중앙값보다 클 경우
            start = mid + 1
    
    return 0

for i in arr2:
    result = b_search(arr1, i, 0, n - 1)
    if result != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')




