from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = {}
        depth = {}
        level_max_height = {}
        level_second_max_height = {}

        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            left_height = dfs(node.left, d + 1)
            right_height = dfs(node.right, d + 1)
            node_height = 1 + max(left_height, right_height)
            height[node.val] = node_height
            if d not in level_max_height or node_height > level_max_height[d]:
                level_second_max_height[d] = level_max_height.get(d, -1)
                level_max_height[d] = node_height
            elif node_height > level_second_max_height.get(d, -1):
                level_second_max_height[d] = node_height
            return node_height

        dfs(root, 0)
        
        answer = []
        tree_height = level_max_height[0]

        for q in queries:
            q_depth = depth[q]
            if height[q] == level_max_height[q_depth]:
                new_height = level_second_max_height[q_depth] + q_depth
            else:
                new_height = tree_height
            answer.append(new_height)

        return answer
