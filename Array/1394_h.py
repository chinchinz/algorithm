class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = []
        for key, val in Counter(arr).items():
            if key == val: res.append(key)
        
        if res : return max(res)
        return -1