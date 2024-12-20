# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        qu = deque([root])
        l = 0

        while qu:
            size = len(qu)
            lev = []

            for _ in range(size):
                node = qu.popleft()
                lev.append(node)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            
            if l % 2 == 1:
                valu = [node.val for node in lev][::-1]
                for i, node in enumerate(lev):
                    node.val = valu[i]
            
            l += 1
        
        return root
