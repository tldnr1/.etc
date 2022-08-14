'''
< 내가 쓴 코드 >
def is_prime(x):
    if x % 2 == 0: return False

    for n in range(3, int(x**(1/2))+1, 2):
        if x % n == 0:
            return False
    return True

def solution(n):
    return len([2] + [num for num in range(3,n+1,2) if is_prime(num)])

'''

# 에라스토테너스의 체 + set의 연산기능 활용
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))  # i의 배수를 num에서 제거
    return len(num)

n = 10
print(solution(n))