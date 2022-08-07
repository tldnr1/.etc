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