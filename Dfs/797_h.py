class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.target = len(graph) - 1
        def dfs(n, path):
            if n == self.target:
                self.res.append(path)
                return
            for i in graph[n]:
                dfs(i, path + [i])
        
        dfs(0, [0])
        return self.res