import heapq

def solution(n, s, a, b, fares):
  ans = 20000001
  
  arr = [[1000001]*n for _ in range(n)]
  for i in range(n):
    arr[i][i] = 0
  for x,y,dist in fares:
    arr[x-1][y-1] = dist
    arr[y-1][x-1] = dist
  

  for i in range(n):
    for j in range(n):
      for k in range(n):
        if arr[j][k] > arr[j][i] + arr[i][k]:
          arr[j][k] = arr[j][i] + arr[i][k]

  q = [(dist, s-1, 0)]
  visit = [False]*n
  visit[s-1] = True
  while q:
    _, node, total = heapq.heappop(q)
    visit[node] = True
    cur_ans = arr[node][a-1]+arr[node][b-1]+total
    if cur_ans < ans:
      ans = cur_ans
    else: continue
    # ans = min(ans, cur_ans)
    for i, dist in enumerate(arr[node]):
      if visit[i]: continue
      # if total+dist > ans: continue
      heapq.heappush(q, (dist, i, total+dist))

  return ans


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))