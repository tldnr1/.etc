def solution(answers): 
  student = {1:[1,2,3,4,5], 2:[2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5,]}
  score = {1:0, 2:0, 3:0}

  for idx, answer in enumerate(answers):
    for k, v in student.items():
      if answer == v[idx % len(v)]:  # idx % len(v)로 student의 answer 순회가능!
        score[k] += 1
        
  max_score = max(list(score.values()))
  return [k for k,v in score.items() if v == max_score]
  
answers = [1,3,2,4,2]
print(solution(answers))