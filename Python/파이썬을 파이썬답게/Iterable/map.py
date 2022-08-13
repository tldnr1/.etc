# e.g. 1 - iterable형 내의 자료형 한번에 바꾸기
list1 = ['1', '100', '3']
answer = []
for value in list1:
  answer.append(int(value))
print(answer)

# 여기에 map을 사용하면
answer = []
answer = list(map(int, list1))
print(answer)