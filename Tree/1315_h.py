# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        q = deque()
        q.append((root, -1))
        
        while q:
            node, parentVal = q.popleft()
            if node.left:
                if parentVal % 2 == 0:
                    ans += node.left.val
                q.append((node.left, node.val))
            if node.right:
                if parentVal % 2 == 0:
                    ans += node.right.val
                q.append((node.right, node.val))

        return ans
            