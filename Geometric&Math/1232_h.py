class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        
        if len(Counter([x for x,y in coordinates]).keys()) == 1 : return True
        if len(Counter([y for x,y in coordinates]).keys()) == 1 : return True
        
        # print(coordinates)
        xDiff, yDiff = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        for i, (x, y) in enumerate(coordinates) :
            if i==0 : continue
            try:
                if (x - coordinates[i-1][0]) / (y - coordinates[i-1][1]) != xDiff / yDiff : return False
            except:
                return False
        return True