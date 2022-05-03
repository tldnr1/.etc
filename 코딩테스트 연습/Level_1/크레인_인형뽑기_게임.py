# < 내가 쓴 코드 >
def solution(board, moves):
  _board = []
  basket = []
    
  n = len(board)
  for i in range(n):
    _board.append([board[j][i] for j in range(n) if board[j][i] != 0])
  # print(_board)
    
    
  ''' 바구니에 담기 '''
  for move in moves:
    try:
      basket.append(_board[move-1][0])
      del _board[move-1][0]
      # print(_board)
    except Exception:
      if len(_board[move-1]) == 0:
        pass
      else:
        return False
    
  ''' 사라진 인형 세기 '''
  # print(basket)
  prev_len = 0
  answer = 0
  while(prev_len != len(basket)):
    prev_len = len(basket)
    for i in range(len(basket)-1):  # 마지막은 빼고 확인
      if basket[i] == basket[i+1]:
        answer += 2
        del basket[i+1]
        del basket[i]
        # print(basket)
        break
                
  return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))