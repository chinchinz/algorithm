from itertools import combinations
from collections import defaultdict

def solution(orders, course):
  ans = []
  orderDict = {}
  for n in course:
    orderDict[n] = defaultdict(int)
    for order in orders:
      order = sorted(list(order))
      for key in combinations(order, n):
        orderDict[n][''.join(key)] += 1
  # print(orderDict)

  for n in course:
    tmp = sorted(orderDict[n].items(), key = lambda item: item[1], reverse=True)
    if not tmp: continue
    M = tmp[0][1]
    for key, val in tmp:
      if val == M and val > 1:
        ans.append(key)
  
  return sorted(ans)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))