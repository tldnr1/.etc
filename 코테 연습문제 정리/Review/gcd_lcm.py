import math

a, b, c = map(int, input().split())

gcd1 = math.gcd(a,b)
lcm1 = a*b // gcd1

gcd2 = math.gcd(lcm1, c)
lcm2 = lcm1*c // gcd2

print(lcm2)

'''
[최대공약수(gcd), 최소공배수(lcm) 알고리즘]

두 수 a, b에 대해서
a * b = gcd(a,b) * lcm(a,b) 가 성립한다

즉, lcm(a,b) = a * b // gcd(a,b) 이다


< 3개 이상의 경우 >
세 수 a, b, c에 대해서  (3 이상에서도 동일)
[a, b, c] == [[a,b], c] 이다.

즉,
gcd(a, b, c) = gcd(gcd(a, b), c)
lcm(a, b, c) = lcm(lcm(a, b), c) 이다

'''