def solution(n):
  n = str(n)
  ans = 100000
  ans_cnt = 100000
  def dfs(n, cnt):
    nonlocal ans
    nonlocal ans_cnt
    # print(n, cnt)
    if len(n)==1:
      if int(n) <= ans:
        ans = int(n)
        ans_cnt = min(cnt, ans_cnt)
    for i,c in enumerate(n[:-1]):
      # if len(n[:i+1]) > 1 and int(n[:i+1]) == 0: continue
      if len(n[i+1:]) > 1 and n[i+1:][0] == '0': continue
      dfs(str(int(n[:i+1])+int(n[i+1:])), cnt+1)
  dfs(n, 0)

  return [max(0, ans_cnt), ans]


print(solution(73425))
print(solution(10007))
print(solution(9))