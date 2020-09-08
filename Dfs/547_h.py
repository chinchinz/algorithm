class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visit = [False] * len(M)
        self.ans = 0
        
        def dfs(k):
            # print('dfs : ', k, M[k])
            for i, friend in enumerate(M[k]):
                if visit[i]: continue
                if not friend: continue
                visit[i] = True
                dfs(i)
        
        for i in range(len(M)):
            if visit[i]: continue
            # print(i)
            self.ans += 1
            visit[i] = True
            dfs(i)
        
        return self.ans