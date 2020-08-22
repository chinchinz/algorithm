class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t :
                prev_idx = stack.pop()
                ans[prev_idx] = i-prev_idx
            stack.append(i)
        return ans