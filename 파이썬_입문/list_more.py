'''
list.index( value ) : 값을 이용하여 위치를 찾는 기능
list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
list.insert( index, value ) : 원하는 위치에 값을 추가
list.sort( ) : 값을 순서대로 정렬
list.reverse( ) : 값을 역순으로 정렬
'''

list = [1, 3, 2]

print(list.index(2))

list.extend([6, 5])
print(list)

list.insert(3, 4)
print(list)

list.sort()
print(list)

list.reverse()
print(list)