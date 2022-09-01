import sys
read = sys.stdin.readline
# 보드판은 aaaa4와 bb2로 채울 수 있다.
st = read() # 보드판을 읽어온다.

st = st.replace('XXXX', 'AAAA')
st = st.replace('XX', 'BB')
if "x" in st:
    print(-1)
else:
    print(st)

