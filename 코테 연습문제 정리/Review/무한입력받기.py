# 백준CodePlus 풀면서 알게 된 내용

# while 문에 try except를 써서 구현

while True:
    try:
        n = int(input())
    except:  # n에 input이 없을 경우 작동함. 즉 입력이 더 없는 경우 프로그램이 종료됨.
        break

    print(n) # 입력을 받았다면 아래에 할 일이 작동되는 형태