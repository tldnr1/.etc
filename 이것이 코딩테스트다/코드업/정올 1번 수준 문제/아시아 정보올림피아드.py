# 순위 정하기 등 주어진 정보로 순번을 결정해야하면
# 무작정 1,2,3 등 판별하는 코드를 짜지 말고
# 1, 2등처럼 앞쪽 순서는 '확정적으로 정해지는 경우'가 있는지 확인해보기

n = int(input())
participant = []
for _ in range(n):
  a, b, c = map(int, input().split())
  participant.append((a,b,c))

participant.sort(key = lambda x: x[2], reverse=True)

# 금메달, 은메달 출력  -> 금, 은메달은 확정적임!
print(participant[0][0], participant[0][1])
print(participant[1][0], participant[1][1])

# 동메달 찾기
i = 2
if participant[0][0] == participant[1][0]:
  world = participant[0][0]
  while world == participant[i][0]:
    i += 1

print(participant[i][0], participant[i][1])