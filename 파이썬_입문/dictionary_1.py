list = {
  'a' : 1,
  'b' : 2,
  'c' : 3
}

print(list)

# 추가하기
list['d'] = 4
print(list)

# 수정하기
list['a'] = 0
print(list)

# 삭제하기
del(list['b'])
print(list)

list.pop('c')
print(list)

print()

# for 문과 함께 사용
"""
keys() : key를 가져옴 <keys()는 생략해도 작동함>
values() : value를 가져옴
items() : key와 value를 가져옴
"""
for key in list:
  print(key, end=' ')
print()

for value in list.values():
  print(value, end=' ')
print()

for key, value in list.items():
  print('{} : {}'.format(key, value), end=' ')
print()