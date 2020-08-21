# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode, depth=0) -> int:
        
        self.ans = 0
        
        def height_of_tree(node):
            if not node:
                return 0
            left_subtree_height = height_of_tree(node.left)
            right_subtree_height = height_of_tree(node.right)
            self.ans = max(self.ans, left_subtree_height+right_subtree_height)
            return 1 + max(left_subtree_height, right_subtree_height)
        
        height_of_tree(root)
        return self.ans
        