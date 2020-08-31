class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        
        res = []
        
        while i < len(A) and j < len(B):
            sA, eA = A[i]
            sB, eB = B[j]
            if sA <= eB and sB <= eA:
                res.append([max(sA, sB), min(eA, eB)])
                
            if eA <= eB:
                i += 1
            else:
                j += 1
        
        return res
