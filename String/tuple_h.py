from collections import defaultdict
from collections import Counter
import re
def solution(s):
    print(Counter(re.findall('\d+', s)))
    print(re.findall('\d+', s))
    d = defaultdict(int)
    s = s[1:-1].split('},')
    for i in range(len(s)):
        s[i] = list(map(int, s[i].strip('{}').split(',')))
        for num in s[i]:
            d[num] += 1
    # print(s)
    # print(d)

    return [key for key,val in sorted([(key, val) for key, val in d.items()], key=lambda x: x[1], reverse=True)]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))