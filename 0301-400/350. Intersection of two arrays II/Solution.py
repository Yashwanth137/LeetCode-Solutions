class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count = Counter(nums1)
        res = []
        
        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
        
        return res
