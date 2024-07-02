class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0, len(nums1)-m):
            nums1.pop()

        for i in range(0, len(nums2)-n):
            nums2.pop()
    
        nums1.extend(nums2)
        nums1.sort()
