class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        d = defaultdict(list)
        for i in range(r):
            for j in range(c):
                d[i-j].append(mat[i][j])
        
        for k in d:
            d[k].sort(reverse=True)
        
        for i in range(r):
            for j in range(c):
                mat[i][j] = d[i-j].pop()
        
        return mat
        