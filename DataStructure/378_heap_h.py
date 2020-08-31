class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        
        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
        
        # print(minHeap)
        
        numberCount, number = 0, 0
        
        while minHeap:
            number, i, row = heappop(minHeap)
            # print(number, i, row)
            numberCount += 1
            if numberCount == k:
                break
            if len(row) > i+1:
                heappush(minHeap, (row[i+1], i+1, row))
        
        return number