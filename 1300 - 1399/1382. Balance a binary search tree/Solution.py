class Solution:
    def balanceBST(self, node: TreeNode) -> TreeNode:
        def traverse(node: TreeNode):
            if node is None:
                return
            traverse(node.left)
            values.append(node.val)
            traverse(node.right)

        def construct(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            middle = (start + end) >> 1
            left_subtree = construct(start, middle - 1)
            right_subtree = construct(middle + 1, end)
            return TreeNode(values[middle], left_subtree, right_subtree)

        values = []
        traverse(node)
        return construct(0, len(values) - 1)
