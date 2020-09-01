class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        
            
        def dfs(k, path):
            if len(path) == 3:
                nonlocal ans
                if path == sorted(path) or path == sorted(path, reverse=True): ans += 1
                return 
            for i in range(k+1, len(rating)):
                dfs(i, path + [rating[i]])
        
        for i in range(len(rating)-2):
            dfs(i, [rating[i]])
        
        return ans
    
