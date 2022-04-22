# divmod : 몫, 나머지 한번에 계산
a, b = map(int, input().strip().split(' '))
print(a//b, a%b)
print(divmod(a,b))  # divmod : 몫, 나머지를 tuple로 반환
print(*divmod(a, b), end='\n\n\n')  # *은 unpacking을 의미

# n진법 -> 10진법
num, base = map(int, input().strip().split(' '))
print(int(str(num), base))

# int의 convert 형태
# int(String, base)
# 예를 들어 3진법 12의 경우 int(str(12), 3) 으로 변환 가능
#                             ㄴ String 타입에 주의할 것!