class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialise final array
        final_array = []

        for first_index, first_num in enumerate(nums):
            # Find corresponding two sum for each number
            two_sum = 0 - first_num
            # Initialise difference dictionary to do two sum
            diff = {}
            for second_index, second_num in enumerate(nums):
                # If the second number is from different location as the first, find the difference
                # and add it to the dictionary
                if second_index != first_index:
                    difference = two_sum - second_num
                    diff[difference] = second_index
            for third_index, third_num in enumerate(nums):
                # Check if a corresponding third number exists
                prev_index = diff.get(third_num, -1)
                # If the number exits, check if the third number is from a different place
                # compared the first and second number selected
                if prev_index != -1 and third_index != first_index and third_index != prev_index:
                    prev_num = nums[prev_index]
                    triplet = sorted([first_num, prev_num, third_num])
                    if triplet not in final_array:
                        final_array.append(triplet)

        return final_array

        