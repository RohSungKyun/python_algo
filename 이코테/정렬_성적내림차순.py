import sys
read = sys.stdin.readline

n = int(read())
arr = []

for i in range(n):
    input_data = read().split()
    arr.append(input_data[0], int(input_data[1]))

arr = sorted(arr, key=lambda student : student[1])

for i in arr:
    print(i, end=' ')