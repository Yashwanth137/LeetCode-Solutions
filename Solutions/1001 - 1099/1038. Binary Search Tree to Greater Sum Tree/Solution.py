class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            nonlocal total
            if node:
                dfs(node.right)
                total += node.val
                node.val = total
                dfs(node.left)
        
        total = 0
        dfs(root)
        return root
