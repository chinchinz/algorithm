class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        curSum = sum(arr[:k])
        threshold *= k 
        if curSum >= threshold : ans += 1
        for i in range(1, len(arr)-k+1):
            curSum = curSum - arr[i-1] + arr[i+k-1]
            if curSum >= threshold : ans += 1
            
        return ans