# for a in b => b에 있는 원소를 a로 하니씩 전달
list = [1, 2, 3]
for number in list:
  print(number)
print()

# range => 필요한 만큼의 수를 만드는 기능
for number in range(5):
  print(number)
print()

# enumerate => 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
names = ['1번 이름','2번 이름', '3번 이름']
for i, name in enumerate(names):
  print('{}번 : {}'.format(i+1, name))