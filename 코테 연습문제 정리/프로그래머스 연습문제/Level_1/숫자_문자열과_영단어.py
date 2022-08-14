'''
< 내가 쓴 코드 >
def solution(s):
    incode = { 'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
             'six':'6', 'seven':'7', 'eight':'8', 'nine':'9' }
    _decode = ''
    decode = []
    answer = []
    
    for word in s:
        if word.isdigit():
            answer.append(word)
        elif word.isalpha():
            decode.append(word)
            _decode = ''.join(decode)
            if _decode in incode:
                answer.append(incode[_decode])
                decode = []
    
    return int(''.join(answer))
'''

# 모범 답안
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

s = 'one4seveneight'
print(solution(s))