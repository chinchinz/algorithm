class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        res = []
        for k in d1:
            if k in d2:
                res.extend([k]*min(d1[k], d2[k]))
        
        return res