''' datetime '''
import datetime as d

# 특정 날짜 지정
christmas_2020 = d.datetime(2020,12,25)
print(christmas_2020)

# 시간 차이 계산
def days_until_christmas():
  christmas_2030 = d.datetime(2030,12,25)
  now = d.datetime.now()
  return (christmas_2030 - now).days

print("{}일".format(days_until_christmas()))
print(end="\n\n")


''' timedelta '''
# 시간 차이를 계산
now = d.datetime.now()
ten_days = d.timedelta(days = 10)
print(type(now))
print(type(ten_days))
print()

# datetime내의 datetime과 timedelta는 서로 계산이 가능하다
print(now)
print(now + ten_days)
print(now - ten_days)
print()


''' replace '''
# 날짜 및 시간을 임의로 변경할 수 있는 함수
# 예시 : 지금으로부터 100일 뒤에 9시 정각을 출력해보기

hundred_after = d.datetime.now().replace(hour=9, minute=0, second=0) + d.timedelta(days = 100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))