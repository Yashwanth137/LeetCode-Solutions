class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        target_sum = skill[0] + skill[-1]
        total_chemistry = 0
        
        left, right = 0, len(skill) - 1
        
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return total_chemistry
