class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            r = target - nums[i]
            if r in nums:
                r = nums.index(r)
                if r != i:
                    if i < r:
                        return  [i, r]
                    else:
                        return [r, i]