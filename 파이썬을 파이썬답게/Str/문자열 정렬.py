# 문자열 정렬 : https://gdnn.tistory.com/237

# 간단한 정렬 함수들 : ljust(), center(), rjust()

str = 'abcd'
n = 7
print(str.ljust(n))
print(str.center(n))
print(str.rjust(n))


''' string에 저장된 기본 상수들 '''
import string
print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters) # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 숫자 0123456789