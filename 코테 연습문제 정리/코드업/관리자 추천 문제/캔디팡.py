# 상,하,좌,우 탐색을 재귀함수로 구현하기! (BFS, DFS 가 재귀함수 알고리즘임!!!!)
# 추가로 flood fill이라는 알고리즘 사용 => 한번 지나간 위치를 0으로 만들어 재탐색을 줄이기!!

board = []

def candy(row, col, color):
  # 범위 밖인 경우
  if row == -1 or col == -1 or row == 7 or col == 7: return 0

  # 다른 색인 경우
  if board[row][col] != color: return 0

  # 같은 색인 경우
  if board[row][col] == color:
    board[row][col] = 0

  # 상,하,좌,우 탐색을 재귀함수를 통해 시행
  return 1+candy(row-1,col,color)+candy(row+1,col,color)+candy(row,col-1,color)+candy(row,col+1,color)


for _ in range(7):
  line = list(map(int,input().split()))
  board.append(line)

cnt = 0
for i in range(7):
  for j in range(7):
    temp = 0
    if board[i][j] != 0:
      temp = candy(i, j, board[i][j])
      
    if temp >= 3: cnt += 1

print(cnt)