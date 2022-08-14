while True:
  try:
    n = int(input())
  except:
    break

  res = 1
  while res % n != 0:
    res = res * 10 + 1
    
  print(len(str(res)))