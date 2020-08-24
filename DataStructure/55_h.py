class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visit = [False] * len(nums)
        q = deque()
        
        visit[0] = True
        q.append(nums[0])
        
        for i in range(len(nums)):
            cur = q.popleft()
            print(cur)
            for j in range(cur, 0, -1):
                print(i, j, cur)
                next_index = i+j
                if next_index >= len(nums)-1 : return True
                if visit[next_index] == True : continue
                q.append(nums[next_index])
        
        return False