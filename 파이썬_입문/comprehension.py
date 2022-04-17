# Comprehension이란?
# list, dict 등과 함께쓰는 for문, if문을 간단하게 쓰는 기능

''' list '''
# 기존의 리스트 생성법
areas = []
for i in range(1,11):
  areas = areas + [i*i]
print("areas:",areas)

# Comprehension을 사용한 리스트 생성법
areas2 = [ i*i for i in range(1,11) ]
print("areas2:",areas2)

# 예1  [ i*i for i in range(1,11) ]   # [ 계산식 for문 ]
# 예2  [ i*i for i in range(1,11) if i % 2 == 0 ]   # [ 계산식 for문 조건문 ]
# 예3  [ ( x, y ) for x in range(15) for y in range(15) ]   # [ 계산식 for문 for문 ]
print(end='\n\n')


''' dict '''
alphabets = ['A', 'B', 'C', 'D', 'E']

# Comprehension을 사용한 딕셔너리 생성법
alphabets_dict = { "{}번".format(number+1) : value for number, value in enumerate(alphabets)}   # [ dict구성 for문 ]

print(alphabets_dict)
print(end='\n\n')


''' zip '''
# list, str 등과 같이 index로 불러올 수 있는 값들을
# zip(a, b)와 같이 묶어서 생성하는 것

subjects = ['국어', '수학', '영어']
students = ['A', 'B', 'C']
scores = ['80', '90', '70']

# zip을 이용한 print문
for x, y in zip(students, scores):
  print('{} : {}'.format(x, y))
print()

# zip을 이용한 딕셔너리 생성법
test_dict = {student : score for student, score in zip(students, scores)}
print(test_dict)

# zip을 이용한 튜플 출력
for x, y, z in zip(subjects, students, scores):
  print(x, y, z)

# zip을 이용한 튜플 생성법
test_tuple = zip(subjects, students, scores)
print(type(test_tuple))    # zip 함수를 쓰면 zip 인스턴스가 생성됨
test_tuple = tuple(test_tuple)    # tuple 대신 list, dict등도 사용 가능 (여긴 3개라 dict 안됨)
print(test_tuple)