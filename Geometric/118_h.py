class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        col = 1
        res = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(col):
                if j==0 or j==col-1:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
            col+=1
        return res