class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num = [1] * n

        # 1. Left pass: Start at 0, move FORWARD, stop at n
        left_product = 1
        i = 0
        while i < n:
            num[i] = left_product
            left_product *= nums[i]
            i += 1  # Move forward

        # 2. Right pass: Start at the end (n - 1), move BACKWARD, stop at 0
        right_product = 1
        i = n - 1
        while i >= 0:
            num[i] *= right_product  # Multiply with existing left product
            right_product *= nums[i]
            i -= 1  # Move backward

        return num