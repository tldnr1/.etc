# Level_1/비밀지도.py

# 문자열 앞,뒤에 원하는 문자 채우기

# 앞 : zfill, rjust
# 뒤 : ljust
'''
zfill(width)
rjust(width, [fillchar])
ljust(width, [fillchar])
'''
print("2".zfill(3))
print("2".rjust(3, '0'))
print("2".ljust(3, '0'))
#               ㄴ 주로 여기에 원하는 길이를 변수로 넣어서 사용