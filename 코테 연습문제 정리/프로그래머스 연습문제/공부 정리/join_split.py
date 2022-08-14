# Level_1/이상한_문자_만들기.py

# join : https://blockdmask.tistory.com/468
# split : https://blockdmask.tistory.com/469

'''
join의 원형 : '구분자'.join(리스트)

구분자에 대해 예를 들어보면,
''.join(['a','b','c']) >> 'abc'
'_'.join(['a', 'b', 'c']) >> 'a_b_c'
' '.join(['a', 'b', 'c']) >> 'a b c'  # ''.join과 ' '.join 구분 잘하기

'''


'''
split의 원형:
1) 문자열.split()
2) 문자열.split('구분자')
3) 문자열.split('구분자', 분할횟수)
4) 문자열.split(seq='구분자', maxsplit=분할횟수)
'''


# 공백이 2칸 있는 list2를 이용하여 차이를 알아보자
list1 = 'a b c'
list2 = 'a b  c'

# 2번에 대해 예를 들어보면,
print(list1.split())  # ['a', 'b', 'c']
print(list2.split())  # ['a', 'b', 'c'] 
                        # 구분자 지정이 없어서 모든 띄워쓰기 생략

print(list1.split(' '))  # ['a', 'b', 'c']
print(list2.split(' '))  # ['a', 'b', ' ', 'c']  # 띄워쓰기 포함됨
                          # 이 차이가 Lv1.이상한 문자 만들기 의 오답 이유!


# 4번에 대해 예를 들어보면, (3번도 동일)
print(list1.split(maxsplit=1))  # ['a', 'b c']
print(list2.split(maxsplit=1))  # ['a', 'b  c']

'''
문자열.split('구분자', 분할횟수)  의 주의사항

문자열.split(1) : 불가능
문자열.split(',', 1) : 가능
문자열.split(maxsplit=1) : 가능
'''