# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return root
        
        q = deque()
        q.append((root, 0))
        
        res = []
        
        while q :
            node, depth = q.popleft()
            if node.left : q.append((node.left, depth+1))
            if node.right : q.append((node.right, depth+1))
            try :
                res[depth].append(node.val)
            except:
                res.append([node.val])
            
        return res
            
            
        