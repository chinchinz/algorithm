from collections import Counter

def solution(nums):
    n = len(nums)
    ans = 0
    d = Counter(nums)
    if len(d.keys()) > n//2: return n//2
    return len(d.keys())





print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))