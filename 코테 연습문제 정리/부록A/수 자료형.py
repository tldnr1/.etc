# 나누기 연산자는 실수형으로 처리됨
a = 6 / 3
print(a)
print(type(a))
print()

# 실수는 보통 round()를 사용해서 처리함
b = round(12.3456,3)
print(b)
print()

# 10의 배수는 '유효숫자e지수 = 유효숫자x10지수' 를 사용
c = 1e9
print(c)
print(round(c))