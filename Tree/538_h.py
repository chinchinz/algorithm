# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         if not root : return root
#         q = deque()
#         q.append(root)
#         nums = []
#         while q :
#             node = q.popleft()
#             nums.append(node.val)
#             if node.left : q.append(node.left)
#             if node.right : q.append(node.right)
        
#         nums.sort()
        
#         q.append(root)
#         while q :
#             node = q.popleft()
#             node.val += sum(nums[nums.index(node.val)+1:])
#             if node.left : q.append(node.left)
#             if node.right : q.append(node.right)
        
#         return root
    
##############################
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.val = 0
        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)
        visit(root)
        return root
            
            