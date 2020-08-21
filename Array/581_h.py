class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 정렬한 list와 비교하여 계산
        res = [i for (i, (a,b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        print(res)
        return 0 if not res else res[-1] - res[0] + 1