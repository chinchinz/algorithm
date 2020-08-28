# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        q = deque()
        q.append((root, 0))
        depths = []
        if root.val == x or root.val == y :
            depths.append((0, None))
        while q:
            node, depth = q.popleft()
            # if node.val == x or node.val == y:
                # depths.append((depth, node.val))
            if node.left : 
                q.append((node.left, depth+1))
                if node.left.val == x or node.left.val == y:
                    depths.append((depth+1, node.val))
                    
            if node.right : 
                q.append((node.right, depth+1))
                if node.right.val == x or node.right.val == y:
                    depths.append((depth+1, node.val))
        print(depths)
        return depths[0][0] == depths[1][0] and depths[0][1] != depths[1][1]