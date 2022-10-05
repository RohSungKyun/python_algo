set1={30, 20, 10, 40, 60, 20, 50, 10}
set2={50, 20, 10, 70, 10, 40, 50}
set3={10, 20, 30}
# 교집합, 합집합, 각각의 차집합
print('set1과 set2의 교집합:',set1&set2)
print('set1과 set2의 합집합:',set1|set2)
print('set1과 set2의 차집합1:',set1-set2)
print('set1과 set2의 차집합2:',set2-set1)
# 부분집합
print('set3가 set1의 부분집합인가요?:', set1>=set3)
print('set3가 set2의 부분집합인가요?:', set2>=set3)
# 원소 추가하기
set2.update(30, 60)
print(set2)
# 원소 삭제하기
set1.remove(50, 60)
print(set1)