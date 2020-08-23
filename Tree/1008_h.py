# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(i, j):
            if i==j: return None
            root = TreeNode(preorder[i])
            mid = bisect.bisect(preorder, preorder[i], i+1, j)
            print(mid)
            root.left = helper(i+1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(preorder))