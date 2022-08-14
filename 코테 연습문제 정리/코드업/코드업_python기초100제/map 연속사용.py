# map(변환기준1, map(변환기준2, 입력값)) 처럼 map을 여러 개 사용가능

# bool(int(input())) 을 map으로 작성
a, b = map(bool, map(int, input().split()))
print(a and b)