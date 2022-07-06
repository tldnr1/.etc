# eval() : 문자열 형식의 수학 수식을 계산
result = eval("(3 + 5) * 7")
print(result)

# sorted() : 정렬, key로 정렬기준 명시, reverse로 역순
list = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(list, key = lambda x: x[1], reverse = True)
print(result)