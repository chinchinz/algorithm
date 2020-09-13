import operator
def solution(maze):
  cnt = 0
  n = len(maze)
  for i in range(n):
    maze[i] = [1] + maze[i] + [1]
  maze.insert(0, [1]*(n+2))
  maze.append([1]*(n+2))
  # print(maze)

  direction = [[1,0], [0,1], [-1,0], [0,-1]]
  # 왼쪽은 그 다음 방향이네
  cur = [1,1]
  idx_d = 0
  list(map(operator.add, cur, direction[idx_d]))
  while True:
    if cur == [n,n]: break
    ny, nx = list(map(operator.add, cur, direction[idx_d]))
    # print(cur)
    # 만약 앞이 벽이라면 turn
    if maze[ny][nx] == 1:
      # print('앞이 벽이라 돌았어요')
      idx_d = (idx_d-1) % 4
      continue
    
    # 만약 왼쪽에 벽이 있으면 간다.
    # ty, tx = list(map(operator.add, cur, direction[(idx_d+1) % 4]))
    # if maze[ty][tx] == 1:
    cur = [ny, nx]
    cnt += 1
    # print('갔어요')
    # 가고 왼쪽에 벽이 없으면 turn
    ty, tx = list(map(operator.add, cur, direction[(idx_d+1) % 4]))
    if maze[ty][tx] == 0:
      idx_d = (idx_d+1) % 4
      # print('벽 없어서 돌았어요', ty, tx, '현재 방향:', direction[idx_d], '현재위치:', cur)

  return cnt


print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]	))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]	))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]	))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]	))