class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start,destination), max(start,destination)
        # print(sum(distance[:start]) + sum(distance[destination:]), sum(distance[start:destination]))        
        return min(sum(distance) - sum(distance[start:destination]), sum(distance[start:destination]))