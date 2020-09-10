def solution(n):
  answer = []
  arr = [[0]*(i+1) for i in range(n)]
  print(arr)
  def triangle(i, j, n, k):
    for x in range(i, n):
      arr[x][0] = k
      k+=1
    for y in range(j, n):
      arr[n-1][j] = k
      while j < n:
        arr[n-1][j] = k
        k += 1
        j += 1
      i -= 2
      while i > 

      # while 

  triangle(0, 0, n, 1)
  print(arr)

  return answer

solution(5)