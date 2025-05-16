class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 = set(nums1) - set(nums2)
        l2 = set(nums2) - set(nums1)

        res = []
        res.append(list(l1))
        res.append(list(l2))

        return res
