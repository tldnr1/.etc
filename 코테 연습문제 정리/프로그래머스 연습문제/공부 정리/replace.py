# Level_1/숫자_문자열과_영단어.py

# replace 참고 블로그 : https://ooyoung.tistory.com/77

'''
형식 : replace(old, new, [count])

- old : 현재 문자열에서 변경하고 싶은 문자

- new: 새로 바꿀 문자

- count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다. 

'''

# e.g.

hello = 'Hello World!'
hi = hello.replace('Hello', 'Hi')
print(hello)
print(hi)


# Level_1/숫자_문자열과_영단어.py 에서의 사용
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)  # key를 value로 교체!
    return int(answer)

s = 'one4seveneight'
print(solution(s))