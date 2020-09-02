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

##########################

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(k, path): 
            # print(path)
            if sum(path) == target: 
                res.append(path)
                return
            if sum(path) > target : return
            for i in range(k, len(candidates)):
                dfs(i, path + [candidates[i]])
        dfs(0, [])
        return res