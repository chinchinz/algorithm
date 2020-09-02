class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(remain, stack):
            if remain == 0:
                res.append(stack)
                return
            
            for item in candidates:
                if item > remain: break
                if stack and item < stack[-1]: continue
                else:
                    dfs(remain - item, stack+[item])
        dfs(target, [])
        return res