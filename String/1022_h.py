# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        ans = 0
        
        def dfs(node, path):
            nonlocal ans
            if node.left == None and node.right == None : 
                path += [node.val]
                ans += int(''.join(map(str, path)), 2)
                return
            
            if node.left : dfs(node.left, path + [node.val])
            if node.right : dfs(node.right, path + [node.val])
        dfs(root, [])
        return ans


#########################

class Solution:
    def sumRootToLeaf(self, root, val=0):
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)