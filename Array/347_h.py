class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print(Counter(nums).most_common())
        
        return [pair[0] for pair in Counter(nums).most_common()[:k]]