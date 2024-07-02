class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
    
        def isMirror(lsub: Optional[TreeNode], rsub: Optional[TreeNode]) -> bool:
            if not lsub and not rsub:
                return True
            if not lsub or not rsub:
                return False
            return (lsub.val == rsub.val and isMirror(lsub.left, rsub.right) and isMirror(lsub.right, rsub.left))

        return isMirror(root.left, root.right)
