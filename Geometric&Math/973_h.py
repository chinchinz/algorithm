class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda k : k[0]*k[0] + k[1]*k[1])
        return points[:K]