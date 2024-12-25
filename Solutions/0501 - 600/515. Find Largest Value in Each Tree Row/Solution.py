# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        qu = deque([root])

        while qu:
            level = len(qu)
            max_el = float('-inf')

            for _ in range(level):
                node = qu.popleft()
                max_el = max(max_el, node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            
            res.append(max_el)
        
        return res
