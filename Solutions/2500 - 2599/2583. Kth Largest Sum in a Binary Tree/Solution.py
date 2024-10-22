class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val:
        self.left = left
        self.right = right

from collections import deque
import heapq

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        
        queue = deque([root])
        level_sums = []

        while queue:
            level_size = len(queue)
            current_level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(current_level_sum)

        if len(level_sums) < k:
            return -1

        max_heap = [-x for x in level_sums]
        heapq.heapify(max_heap)

        for _ in range(k - 1):
            heapq.heappop(max_heap)

        return -heapq.heappop(max_heap)
