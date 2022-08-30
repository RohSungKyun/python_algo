# 후위표기식
import sys
read = sys.stdin.readline
n = int(read())
string = list(read().rstrip())
nums = [int(read()) for i in range(n)]
stack=[]
for tmp in string:
    if tmp.isalpha():
        stack.append(nums[ord(tmp)-65])
    elif tmp in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        stack.append(eval(f'{a}{tmp}{b}'))

print(f"{stack[0]:.2f}")

