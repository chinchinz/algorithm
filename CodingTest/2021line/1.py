def solution(boxes):
  ans = 0
  for i in range(len(boxes)):
    boxes[i].sort()
  boxes.sort()

  for i,(a,b) in enumerate(boxes[:-1]):
    if a == b: continue
    if a in boxes[i+1]:
      boxes[i][1], boxes[i+1][0] = boxes[i+1][0], boxes[i][1]
    elif b in boxes[i+1]:
      boxes[i][0], boxes[i+1][0] = boxes[i+1][0], boxes[i][0]
  
  for a,b in boxes:
    if a!=b: ans += 1

  return ans


print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]	))
print(solution([[1, 2], [2, 3], [3, 1]]	))