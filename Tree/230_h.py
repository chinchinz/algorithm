# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.i = 0
        self.ans = 0
        def dfs(node):
            if self.ans != 0: return
            if node.left : dfs(node.left)
            self.i+=1
            # print(self.i)
            if self.i == k : 
                self.ans = node.val
                return
            if node.right : dfs(node.right)
        
        dfs(root)
        return self.ans


###########STACK################

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s = []
        
        while root or s:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            k -= 1
            if k==0:
                return root.val
            root = root.right