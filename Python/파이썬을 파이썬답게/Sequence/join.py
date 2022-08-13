# join을 이용한 sequence 이어붙이기
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value
print(answer)
  
# 위의 코드를
my_list2 = ['2', '200', '66']
answer2 = ''.join(my_list2)
print(answer2, end='\n\n')


# * 를 str에 사용하여 여러번 반복해주기
'''
3을 입력받고
*
**
*** 출력하기
'''

n = 3
for i in range(n):
  print('*' * i)


# * 를 이용하면 같은게 반복되는 리스트도 만들 수 있음
list = [123, 456]
new_list = [123, 456] * 3
print(new_list)