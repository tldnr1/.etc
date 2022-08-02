def SuperSum(k, n):
  if k == 0:
    return n
  else:
    superSum = 0
    for i in range(1,n+1):
      superSum += SuperSum(k-1,i)
    return superSum

while(True):
  try:
    k, n = map(int, input().split())
    print(SuperSum(k,n))
  except:
    break