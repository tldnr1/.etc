# 두 개의 정수가 한 줄에 입력되는 경우
# 입력 : 1, 2

a, b = map(int, input().split())
print(a, b)

# strip([char]) : 문장에서 [char]을 모두 삭제
# lstrip([char]) : 문장의 선행부분에서 [char]을 모두 삭제
# rstrip([char]) : 문장의 후행부분에서 [char]을 모두 삭제

str = 'AAhelloAA'
print(str.strip('A'))
print(str.lstrip('A'))
print(str.rstrip('A'))