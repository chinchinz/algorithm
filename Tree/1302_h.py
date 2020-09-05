# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#         res = []
        
#         def dfs(node, depth):
#             nonlocal res
#             if not node.left and not node.right:
#                 res.append((node.val, depth))
#                 return
            
#             if node.left : dfs(node.left, depth+1)
#             if node.right : dfs(node.right, depth+1)
        
#         dfs(root, 0)
#         res.sort(key=lambda k:k[1], reverse=True)
#         maxDepth = res[0][1]
#         return sum(val for val, depth in res if depth == maxDepth)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        while True:
            q_new = [ x.left for x in q if x.left ] 
            q_new += [ x.right for x in q if x.right ] 
            if not q_new:
                break
            q = q_new
        return sum([ node.val for node in q ])