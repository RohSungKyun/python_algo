from os import major


print("이름을 입력하세요:", end=' ')
name = input()
print("학번을 입력하세요:", end=' ')
student_num = int(input())
print("학과를 입력하세요:", end=' ')
department = input()
print("학교를 입력하세요:", end=' ')
univ = input()
print("학년을 입력하세요:", end=' ')
uy = int(input())
print()

print("<출력>")
print("이름: %s"%(name))
print("학번: %d"%(student_num))
print("학과: %s"%(department))
print("학교: %s"%(univ))
print("학년: %d"%(uy))