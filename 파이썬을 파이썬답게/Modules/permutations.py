import itertools

mylist = [2, 3, 1]
mylist.sort()
answer = list(map(list, itertools.permutations(mylist)))
print(answer)

# 2개의 원소만 이용해서 하는 경우
print(list(map(list, itertools.permutations(mylist,2))))


# combinations(조합)도 비슷하게 사용 가능
print(list(map(list, itertools.combinations(mylist,3))))  # 조합은 뒤의 인자 필수!
print(list(map(list, itertools.combinations(mylist,2))))


# permutations(순열)은 원소가 중복되어도 다르다고 보지만 [1,2,3] != [3,2,1]
# combinations(조합)도 원소가 중복되면 같다고 봄 [1,2,3] == [3,2,1]

# permutations(iterable, r=None)
# combinations(iterable, r)   # r이 필수로 들어가야 한다는 의미