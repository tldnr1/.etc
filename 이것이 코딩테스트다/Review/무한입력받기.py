# 백준CodePlus 풀면서 알게 된 내용

# while 문에 try except를 써서 구현

while True:
    try:
        n = int(input())
        print(n)
    except:  # n에 input이 없을 경우 작동함. 즉 입력이 더 없는 경우 프로그램이 종료됨.
        break
