from collections import deque
def solution(balls, orders):
  ans = []

  balls = deque(balls)
  waitQueue = set()

  for order in orders:
    if order == balls[0]:
      ans.append(balls.popleft())
    elif order == balls[-1]:
      ans.append(balls.pop())
    else:
      waitQueue.add(order)
    
    while balls and balls[0] in waitQueue:
      ans.append(balls.popleft())
      waitQueue.remove(ans[-1])
    while balls and balls[-1] in waitQueue:
      ans.append(balls.pop())
      waitQueue.remove(ans[-1])

    # print(order, ans, waitQueue, balls)

  return ans


print(solution([1, 2, 3, 4, 5, 6]	, [6, 2, 5, 1, 4, 3]	))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))
# print(solution())