# 문자열을 모두 같은 수로 채우는 것

import sys
read = sys.stdin.readline
s = list(read().strip())
zero, one = 0, 0

for i in range(len(s)):
    if s[i] == '0' and i == 0 or  s[i-1]== '1' and s[i]=='0':
        zero+=1
    elif s[i] == '1' and i == 0 or s[i-1] == '0' and s[i]=='1':
        one+=1

print(min(zero, one))
