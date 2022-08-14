dic = {}

def SuperSum(k, n):
  if (k,n) in dic:
    return dic[(k,n)]

  if k == 0:
    dic[(0,n)] = n
    return n
  else:
    dic[(k,n)] = sum([SuperSum(k-1,i) for i in range(1,n+1)])
    return dic[(k,n)]

while(True):
  try:
    k, n = map(int, input().split())
    print(SuperSum(k,n))
  except:
    break


# 1. dict의 key는 변경 불가능 이여야 함
#     ㄴ key에 '튜플' 사용가능!

# 2. 메모이제이션(Memoization)
#      line 4~5 처럼, 이미 한번 계산했던 값은 저장해서
#      다시 이 값을 계산해야 할 때 계산하지 않고 값을 불러와 시간을 단축하는 기법