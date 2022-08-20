import sys
read = sys.stdin.readline
# 9 명의 난쟁이 중 2명의 스파이를 찾아내자 => 2명의 키의 합이 total-100의 값이 나올 것이다.
arr =[]
for i in range(9):
    arr.append(int(read()))


total=sum(arr)

u, v = -1, -1
for i in range(9):
    for j in range(i+1, 9):
        if arr[i]+arr[j] == total-100:
            u, v = arr[i], arr[j]
arr.sort() # 오름차순 출력해야 한다.
for i in arr:
    if i==u or i==v:
        continue
    print(i)
