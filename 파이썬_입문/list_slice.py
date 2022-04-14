'''
slice를 하면 해당하는 부분의 리스트나 문자열을 새로 만들어 준다.

* 시작과 끝부분을 얻어 오는 방법
    list[ 2: ] : 2번째부터 끝까지 반환
    list[ : 2 ] : 처음부터 2번째 까지 반환
    list[ : ] : 처음부터 끝까지 전부 반환

* slice의 최종 형태 (step은 음수도 된다!)
    list[start:end:step]
'''

rainbow = ['빨', '주', '노', '초', '파', '남', '보']
print(rainbow[2:])  # 2 ~ length-1
print(rainbow[:2])  # 0 ~ 2-1
print(rainbow[-2:]) # length-2 ~ length-1 = 5 ~ 6

# list[a:b] = a부터 b번째(위치상 b-1) 까지 반환
# 따라서 list(a) --- list(b-1)까지 반환됨

list1 = list(range(20))

# 5, 8, 11, 14 출력
print(list1[5:15:3])

# step은 음수여도 된다!
# 17, 13, 9, 5 출력
print(list1[17:4:-4])


list1 = [0, 1, 2, 3, 4, 5]
# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11, 22, 33]


list2 = [0, 1, 2, 3, 4, 5]
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del list2[1:4]

print("list1 : {}, list2 : {}".format(list1, list2))