max_people = 0
on_train = 0

for _ in range(10):
  x, y = map(int, input().split())
  on_train += y-x

  if max_people < on_train:
    max_people = on_train

print(max_people)