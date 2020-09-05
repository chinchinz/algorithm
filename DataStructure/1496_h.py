class Solution:
    def isPathCrossing(self, path: str) -> bool:
        move = 'NSEW'
        cur = [0,0]
        pointSet = set([tuple(cur)])
        for p in path :
            if p == 'N':
                cur[1] += 1
            elif p == 'S':
                cur[1] -= 1
            elif p == 'E':
                cur[0] -= 1
            elif p == 'W':
                cur[0] += 1
            
            if tuple(cur) in pointSet: return True
            pointSet.add(tuple(cur))
            # print(pointSet)
        
        return False