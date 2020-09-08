class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 0
        ans = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                cur = i+1
                while cur < len(s) and s[cur] == s[i]:
                    cur += 1
                # print(i, cur, sum(cost[i:cur]), max(cost[i:cur]))
                ans += sum(cost[i:cur]) - max(cost[i:cur])
                i = cur-1
            i+=1
        
        return ans