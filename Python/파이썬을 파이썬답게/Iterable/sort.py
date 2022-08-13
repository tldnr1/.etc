mylist = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]
print(len(mylist))  # list의 길이 == 행의 개수
print(len(mylist[0]))  # list[0]의 길이 == 열의 개수


# 원본 리스트를 건드리지 않는 sorted!
# sort 함수는 리스트의 순서를 다 바꿔버림
list1 = [3, 2, 5, 1]
list2 = sorted(list1)  # list1의 순서는 건드리지 않고 list2에 정렬해줌
print(list1)
print(list2)


''' zip 함수 '''
# 리스트에서 행과 열을 바꾸기
# c언어 버전
list1 = [[1,2,3], [4,5,6], [7,8,9]]
answer = [[], [], []]
for i in range(len(list1)):
  for j in range(len(list1[0])):
    answer[i].append(list1[j][i])
print(answer)

# zip 함수를 사용한 버전
new_list = list(zip(*list1))
print(new_list)
print(type(new_list))
print(type(new_list[0]))  # 겉만 list이고 속은 tuple임

new_list2 = list(map(list, zip(*list1)))  # map을 사용하면 내부까지 list화 가능
print(new_list2)