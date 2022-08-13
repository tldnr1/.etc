# Level_1.md 의 최소직사각형

# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
'''
< 내가 쓴 코드 >
def solution(sizes):
    x = []
    y = []
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        x.append(size[0])
        y.append(size[1])
    
    return max(x) * max(y)
'''

'''
def solution(sizes):
  return max(max(x) for x in sizes) * max(min(x) for x in sizes)

위와 같이 max의 max를 하면 sizes의 각 원소들에서 가져온 max 중의 max를 구할 수 있음
min의 max도 비슷한 의미

즉 for문에서 값을 모아두고 max를 돌리는걸 한 줄로 표현 가능함
'''