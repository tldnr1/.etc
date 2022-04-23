# sort(), sorted() 에 대한 정보 : https://infinitt.tistory.com/122
# lambda 에 대한 정보 : https://wikidocs.net/64

#my_str = input().strip()
my_str = 'dedffdgf'
count = {}
for element in my_str:
    try:
        count[element] += 1
    except:
        count[element] = 1

count = dict(sorted(count.items(), key=lambda item:item[0]))
print(count)
sorted_count = sorted(count.items(), key=lambda item:item[1], reverse=True)

answer = ""
cnt=0
for x, y in sorted_count:
    if y >= cnt:
        cnt = y
        answer += x
    else:
        break
        
print(answer)


'''
[모범 답안 - level 상]
from collections import Counter

my_str = input().strip()
max_count = max(Counter(my_str).values())
print(''.join(sorted([k for k,v in Counter(my_str).items() if v == max_count])))
'''

from collections import Counter

Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

print(Counter('hello world'))