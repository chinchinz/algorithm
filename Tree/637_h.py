# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        q = deque()
        q.append((root, 0))
        
        while q:
            node, depth = q.popleft()
            if len(res) < depth + 1:
                res.append([node.val, 1])
            else:
                res[depth][0] += node.val
                res[depth][1] += 1
            
            if node.left : q.append((node.left, depth+1))
            if node.right : q.append((node.right, depth+1))
        return [val/count for val, count in res]