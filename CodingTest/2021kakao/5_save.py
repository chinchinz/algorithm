def solution(play_time, adv_time, logs):
  ans = 0
  ans_time = 0
  def toSecond(li):
    li = list(map(int, li.split(':')))
    return 3600*li[0] + 60*li[1] + li[2]
  
  play = toSecond(play_time)
  adv = toSecond(adv_time)
  if play == adv: return '00:00:00'
  arr = [0]*play
  for log in logs:
    s, e = map(toSecond, log.split('-'))
    for i in range(s,e):
      arr[i] += 1
  
  ans = sum(arr[:adv])
  cur = ans
  for i in range(adv, play):
    cur += arr[i]
    cur -= arr[i-adv]
    if cur > ans:
      ans = cur
      ans_time = i-adv

  ans_time += 1
  h = ans_time // 3600
  ans_time -= 3600*h
  m = ans_time // 60
  ans_time -= 60*m
  ans_list = [str(h).zfill(2),str(m).zfill(2),str(ans_time).zfill(2)]
  
  return ':'.join(ans_list)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))