import math
def solution(distance, rocks, n):
  rocks.sort()
  rocks.append(distance)
  l, r = 0, distance
  ans = 0
  while l <= r:
    prev = 0
    mins = math.inf
    removed_rocks = 0

    mid = (l+r) // 2

    for i in range(len(rocks)):
      if rocks[i] - prev < mid:
        removed_rocks += 1
      else:
        mins = min(mins, rocks[i] - prev)
        prev = rocks[i]

    if removed_rocks > n:
      r = mid - 1
    
    else:
      ans = mins
      l = mid + 1
  
  return l-1

print(solution(25, [2,14,11,21,17],2))