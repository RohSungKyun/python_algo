sentence = input('문자열 입력 :')

# 공백 없애고 대입하기
sentence = sentence.strip()
print(sentence)
# 문자열 슬라이싱하여 초기화
slice1 = sentence[:12]
slice2 = sentence[14:17]
slice3 = sentence[19]
slice4 = sentence[21]
sentence = slice1 + slice2 + slice3 + slice4
print(sentence)
# 문자열 길이 출력
print('변경된 문자열의 길이:',len(sentence))
# 대소문자로 출력
print(sentence.lower())
print(sentence.upper())
# 내 이름으로 대체
print(sentence.upper().replace("MR. HODY","MS. 김땡땡"))