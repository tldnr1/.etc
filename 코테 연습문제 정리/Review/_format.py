# 참고 사이트 : https://systemtrade.tistory.com/373

''' 실수 자릿수 지정 방법'''
math = 75.42
science = 82.127

# 1) '%.2f' % () 사용
print('math : %.1f, science = %.2f' % (math, science))

# 2) format 사용, {주소값 : 자릿수} 형태
print('math : {0:.1f}, science = {1:.2f}'.format(math, science))

# 3) round(수, 자릿수)  => 문장에 끼워넣기 힘들어짐
print('math :', round(math,1), 'science =', round(science,2))