class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if node:
                traverse(node.left)   
                traverse(node.right)  
                result.append(node.val) 
        
        traverse(root)
        return result
