class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 : return 0
        matrix = [[int(a) for a in row] for row in matrix]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0 : continue
                if matrix[i-1][j-1] > 0 and matrix[i-1][j] > 0 and matrix[i][j-1] > 0 :
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1
        return max(map(max, matrix))**2