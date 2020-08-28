class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0 : continue
                if matrix[i-1][j] > 0 and matrix[i][j-1] > 0 and matrix[i-1][j-1] > 0 :
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
        # print(matrix)
        return sum([sum(a) for a in matrix])