# deque로 큐를 구현, 시간복잡도 O(1)

# 가장 앞쪽에 원소 추가     : appendleft(x)
# 가장 뒤쪽에 원소 추가     : append(x)
# 가장 앞쪽에 있는 원소 제거 : popleft()
# 가장 뒤쪽에 있는 원소 제거 : pop()

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))
print()

# Counter는 등장 횟수를 세는 기능을 제공
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))
