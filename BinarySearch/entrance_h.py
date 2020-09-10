def solution(n, times):
  l = 1
  r = max(times) * n

  while l <= r:
    mid = (l+r)//2
    cnt = sum(mid//time for time in times)
    # print(cnt)
    if cnt < n:
      l = mid+1
    elif cnt >= n:
      r = mid-1

  return l


print(solution(6, [7,10]))