# 생태학
import sys
read = sys.stdin.readline

dic = {}
cnt=0

while True:
    tree = read()
    if not tree:
        break
    try:
        dic[tree]+=1
        cnt+=1
    except:
        dic[tree]=1
        cnt+=1

dic = sorted(dic.items())
for key, value in dic:
    print('%s %.4f'%(key, value/cnt*100))