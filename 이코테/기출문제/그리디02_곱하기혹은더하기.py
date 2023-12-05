# 주어진 0 - 9 문자열 사이에 곱하기, 더하기를 넣어 가장 큰 수를 구하여라
# 모든 연산은 우선순위와는 상관없이 왼쪽에서 부터 이루어진다.
# 연산자 사용에는 제한이 없다.

import sys
read = sys.stdin.readline
s = str(read()).strip() # 줄바뀜 제거

ans = 0
for i in range(1, len(s)):
    tmp = int(s[i])
    if tmp<=1 or ans<=1:
        ans+=tmp
    else:
        ans*=tmp
print(ans)