class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        srcList = [0]*(N+1)
        dstList = [0]*(N+1)
        for src, dst in trust:
            srcList[src] += 1
            dstList[dst] += 1
        
        # print(srcList, dstList)
        
        for i in range(1, N+1):
            if srcList[i] == 0 and dstList[i] == N-1:
                return i
        
        return -1