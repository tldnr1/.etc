list1 = [1, 2, 3]
print('list1 :', list1)
print()

# list 를 더하면 새로운 리스트를 만듬
list2 = list1 + [4]
print('list1 :', list1)
print('list2 :', list2)
print()

# append 를 이용하면 기존 list에 값을 추가
list1.append(4)
print('list1 :', list1)
print('list2 :', list2)
print()

# del 을 이용하여 list의 특정 위치를 삭제
del list1[-2]
print('list1 :', list1)
print('list2 :', list2)
print()

# remove 를 이용하여 list에서 특정 값을 삭제
# 단, 값이 여러개면 앞에서부터 1개만 삭제
list2.remove(2)
print('list1 :', list1)
print('list2 :', list2)