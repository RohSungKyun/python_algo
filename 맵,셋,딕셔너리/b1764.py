import sys
read = sys.stdin.readline
# 듣보잡 문제

n, m = map(int, read().split())

arr1 = [0]*n
arr2 = [0]*m

# 보지도 못한 사람을 저장하는 배열
for i in range(n):
    arr1[i] = read().rstrip() # \n줄바꿈 제거해주기
for n in range(m):
    arr2[n] = read().rstrip()

intersection = list(set(arr1)&set(arr2)) # 교집합을 반환
print(len(intersection))
intersection.sort()
for i in range(len(intersection)):
    print(intersection[i])