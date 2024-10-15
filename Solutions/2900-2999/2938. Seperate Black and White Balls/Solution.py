class Solution:
    def minimumSteps(self, s: str) -> int:
        indices = [i for i, char in enumerate(s) if char == '1']
        
        sorted_s = sorted(s)
        target_indices = [i for i, char in enumerate(sorted_s) if char == '1']
        
        steps = 0
        for i in range(len(indices)):
            steps += abs(indices[i] - target_indices[i])
        
        return steps
