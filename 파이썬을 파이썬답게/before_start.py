# 파이썬 list 입력받기 심화!
# https://sunho-doing.tistory.com/27
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline (조금 더 심화)

"""import sys

def solution(mylist):
    answer = []
    for row in mylist:
        answer.append(len(row))
    return answer

mylist = [list(sys.stdin.readline().split())]
print(mylist)
print(solution(mylist))"""

# 위의 것을 Python스럽게 하면
def solution(mylist):
  return list(map(len, mylist))

mylist = [[1,2], [3,4], [5]]
print(solution(mylist))

# map 함수
#  ㄴ map(변환 함수, 순회 가능한 데이터)