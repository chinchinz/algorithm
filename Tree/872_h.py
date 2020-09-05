# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node, s, li):
            while s:
                node = s.pop()
                if not node.left and not node.right:
                    li.append(node.val)
                if node.right : s.append(node.right)            
                if node.left : s.append(node.left)
            return li
        return dfs(root1, [root1], []) == dfs(root2, [root2], [])        