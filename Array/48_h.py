class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r//2):
            matrix[i], matrix[r-i-1] = matrix[r-i-1], matrix[i]
        
        # print(matrix)
        
        for i in range(r):
            for j in range(i, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # print(matrix)
        
        
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])