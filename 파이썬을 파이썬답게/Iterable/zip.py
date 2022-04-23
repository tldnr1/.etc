'''
zip 함수에 대한 영어 설명 :
  Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
'''

# e.g. 1 - 여러 개의 Iterable 동시에 순회할 때 사용
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)
# e.g. 2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기
# 파이썬의 zip 함수와 dict 생성자를 이용하면 코드 단 한 줄로, 두 리스트를 합쳐 딕셔너리로 만들 수 있습니다.
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
print()
print(answer)



# zip 함수로 index 순회
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i] - mylist[i+1]))
    return answer

# 여기에 zip을 사용하면,
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer
# 위와 같이 가능함.
''' 주의! zip 함수에 서로 길이가 다른 리스트가 인자로 들어오는 경우에는 길이가 짧은 쪽 까지만 이터레이션이 이루어집니다. '''