# Level_1.md 의 실패율 등

# 참고한 자료 : https://codechacha.com/ko/python-sorting-dict/
#              Level_1 중 실패율의 다른 사람의 풀이

dict = {'a':1, 'b':3, 'c':2, 'e':4}

# 위의 dict를 value를 기준으로 역순 정렬하기
sorted_dict1 = sorted(dict.items(), key = lambda item:item[1], reverse=True)
print(sorted_dict1)

# key를 통해 value만 뽑아서 정렬하기
sorted_dict2 = sorted(dict, key = lambda x:dict[x], reverse=True)
print(sorted_dict2)
''' sorted에 dict를 넣었다. dict는 dict.keys()를 의미한다.
    여기서 key의 lambda에 dict[x]는 딕셔너리[키] 이므로 value이다! '''