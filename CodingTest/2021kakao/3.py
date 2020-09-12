from bisect import bisect_left
from collections import defaultdict
import re

def solution(infos, querys):
  ans = []
  d = {'java':{'backend':{'junior':{'chicken':[], 'pizza':[]}, 'senior':{'chicken':[], 'pizza':[]}}, 'frontend':{'junior':{'chicken':[], 'pizza':[]}, 'senior':{'chicken':[], 'pizza':[]}}},\
       'cpp':{'backend':{'junior':{'chicken':[], 'pizza':[]}, 'senior':{'chicken':[], 'pizza':[]}}, 'frontend':{'junior':{'chicken':[], 'pizza':[]}, 'senior':{'chicken':[], 'pizza':[]}}}, \
       'python':{'backend':{'junior':{'chicken':[], 'pizza':[]}, 'senior':{'chicken':[], 'pizza':[]}}, 'frontend':{'junior':{'chicken':[], 'pizza':[]}, 'senior':{'chicken':[], 'pizza':[]}}}}
  for info in infos:
    tmp = d
    li = info.split()
    li[-1] = int(li[-1])
    for word in li[:-2]:
      tmp = tmp[word]
    tmp[li[-2]].insert(bisect_left(tmp[li[-2]], li[-1]), li[-1])

  def countQuery(d, query):
    cnt = 0
    flag = False
    tmp = d
    for i, q in enumerate(query[:-1]):
      if q == '-':
        for key in tmp.keys():
          cnt += countQuery(tmp[key], query[i+1:])
          flag = True
        break
      else:
        tmp = tmp[q]
    if flag : return cnt
    cnt = len(tmp) - bisect_left(tmp, int(query[-1]))
    return cnt
  
  for query in querys:
    query = re.split(r' and | \s', query)
    query.extend(query.pop().split(' '))
    ans.append(countQuery(d, query))

  return ans


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], \
  ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], \
#   ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200"]))
# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], \
#   ["- and - and - and - 150"]))


# print(solution())
# print(solution())