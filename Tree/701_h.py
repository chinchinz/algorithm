# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root : return TreeNode(val)
        
        node = root
        
        while node:
            if node.val > val:
                if not node.left: 
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root