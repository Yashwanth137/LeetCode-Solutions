class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) < 2:
                return nums
            
            low, mid, high = [], [], []
            pivot = nums[randint(0, len(nums)-1)]
            for i in nums:
                if i < pivot:
                    low.append(i)
                elif i == pivot:
                    mid.append(i)
                else:
                    high.append(i)

            return quicksort(low) + mid + quicksort(high)
        
        res = quicksort(nums)
        return res
