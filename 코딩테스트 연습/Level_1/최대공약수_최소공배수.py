# gcd 설명 : https://brownbears.tistory.com/454

from math import gcd
def solution(n, m):
  _gcd = gcd(n, m)
  return [_gcd, n*m // _gcd]

n = 3
m = 12
print(solution(n, m))