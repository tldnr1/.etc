# 삼항 연산자 : True값 if 조건 else False값

# b >= a 인 경우 True, 아니면 False
a, b = map(int, input().split())
print('True' if b >= a else 'False')

# a, b, c 중 가장 작은 값 찾기
# 알고리즘 : (a,b 중 작은값 고름) -> c랑 비교
#             ㄴ (a,b중 작은값) if (a,b중 작은값)<c else c
a, b, c = map(int, input().split())
print((a if a<b else b) if (a if a<b else b)<c else c)