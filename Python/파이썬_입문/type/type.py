list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
  print('당연히 list1과 list1은 동일함')

if list1 == list2:
  print('list1과 list2의 값은 동일함')
  if list1 is list2:
    print('list1과 list2는 같은 인스턴스이다')
  else:
    print('list1과 list2는 다른 인스턴스이다')

# 위의 예시처럼
# == 은 값을 비교하지만
# is 는 같은 인스턴스인지 확인함