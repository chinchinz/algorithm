from collections import defaultdict
def solution(companies, applicants):
  ans = defaultdict(list)
  for i in range(len(companies)):
    companies[i] = companies[i].split(' ')
  
  for i in range(len(applicants)):
    applicants[i] = applicants[i].split(' ')
  
  # print(companies)
  # print(applicants)
  i = 0
  while i < 5:
    try:
      d = defaultdict(list)
      for i, applicant in enumerate(applicants):
        # print(applicant)
        most = applicants[i][1][0]
        applicants[i][1] = applicants[i][1][1:]
        d[most].append(applicant[0])
      # print(d)
      for i,companie in enumerate(companies):
        if companie[2] == '0': continue
        for apply in companie[1]:
          if apply in d[companie[0]]:
            ans[companie[0]].append(apply)
            companies[i][2] = str(int(companies[i][2]) -1)
            if companies[i][2] == '0' : break
    except:
      break

    ansans = []
    for key in ans.keys():
      ans[key].sort()
      ansans.append(key+'_'+''.join(ans[key]))
    # print(ans)
    i+=1 
  return ansans


print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]	))
# print(solution())
# print(solution())