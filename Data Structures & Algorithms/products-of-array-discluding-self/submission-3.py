class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = [1] * len(nums)
        left_product = [1] * len(nums)
        final_product = [1] * len(nums)

        for i in range(len(nums)):
            if i != 0:
                right_product[i] = right_product[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                left_product[i] = left_product[i + 1] * nums[i + 1]

        # print(left_product)
        for i in range(len(nums)):
            final_product[i] = right_product[i] * left_product[i]

        return final_product


        