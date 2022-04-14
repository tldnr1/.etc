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

'''
리스트와 문자열 : 서로 비슷하다
  list = str.split( ) : 문자열에서 리스트로
  " ".join( list ) : 리스트에서 문자열으로

e.g.
  list = str.split(":")     #문자열을 ":"기준으로 리스트화
  new_str = ":".join(list)  #리스트를 ":"기준으로 문자열화
'''

print()
print('List & String')

# 오늘은 날씨가 맑음 -> 오늘은 날씨가 흐림
word = '오늘은 날씨가 맑음'

word_list = word.split( )  # 공백을 기준으로 리스트화
print(word_list)

position = word_list.index('맑음')  # list에서 맑음의 위치를 찾아옴
print(position)
word_list[position] = '흐림'

new_word = ' '.join(word_list)  # 공색을 기준으로 문자열화
print(new_word)