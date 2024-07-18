# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes_map = {}

        def traverse(node, parent):
            node.parent = parent
            nodes_map[node.val] = node
            if node.left:
                traverse(node.left, node)
            if node.right:
                traverse(node.right, node)

        traverse(root, None)

        q = [(startValue, '')]
        seen = set()
        while q:
            new_q = []
            for v, t in q:
                if v in seen:
                    continue
                seen.add(v)
                if v == destValue:
                    return t
                node = nodes_map[v]
                for next_node, direction in [(node.parent, 'U'), (node.left, 'L'), (node.right, 'R')]:
                    if next_node and next_node.val not in seen:
                        new_q.append((next_node.val, t + direction))
            q = new_q

        raise ValueError("not found")



    def getDirections0(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj_list = defaultdict(list)

        def traverse(node):
            if node.left:
                adj_list[node.val].append((node.left.val, 'L'))
                adj_list[node.left.val].append((node.val, 'U'))
                traverse(node.left)
            if node.right:
                adj_list[node.val].append((node.right.val, 'R'))
                adj_list[node.right.val].append((node.val, 'U'))
                traverse(node.right)
        
        traverse(root)

        q = deque([(startValue, '')])
        seen = set()
        while q:
            v, t = q.popleft()
            if v in seen:
                continue
            seen.add(v)
            if v == destValue:
                return t
            for w, d in adj_list[v]:
                if w in seen:
                    continue
                q.append((w, t + d))

        raise ValueError("not found")

