import math

a, b, c = map(int, input().split())

gcd1 = math.gcd(a,b)
gcd2 = math.gcd(b,c)

print(math.gcd(gcd1, gcd2))