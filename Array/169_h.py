class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # print(Counter(nums).most_common(1))
        for key, val in Counter(nums).items():
            if val > len(nums)//2 : return key

'''
most_common()
value 내림차순으로 정렬
'''