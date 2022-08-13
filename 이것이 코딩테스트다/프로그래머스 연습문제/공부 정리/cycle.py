# Level_1/모의고사.py

# cycle 설명 블로그 : https://blog.fakecoding.com/archives/python-cycle
# cycle 공식 레퍼런스 : https://docs.python.org/3/library/itertools.html

'''
모의고사.py 중에서 아래와 같이 반복되는 리스트가 있었음
student = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5,]}

이때, v[idx % len(v)]:  # idx % len(v)로 student의 answer 순회가능!
와 같이 사용하였었음 (자세한 건 '모의고사.py' 참고)

여기에서 cycle을 사용해서 리스트를 무한으로 만드는 방법도 존재!

from itertools import cycle

giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
'''