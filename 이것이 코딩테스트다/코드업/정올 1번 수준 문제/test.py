n = int(input())
participant = []
for _ in range(n):
  a, b, c = map(int, input().split())
  participant.append((a,b,c))

participant.sort(key = lambda x: x[2], reverse=True)

# 금메달, 은메달 출력
print(participant[0][0], participant[0][1])
print(participant[1][0], participant[1][1])

# 동메달 찾기
i = 2
if participant[0][0] == participant[1][0]:
  world = participant[0][0]
  while world == participant[i][0]:
    i += 1

print(participant[i][0], participant[i][1])