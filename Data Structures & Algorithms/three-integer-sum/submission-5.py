class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialise final array
        final_array = []

        for first_index, first_num in enumerate(nums):
            # Find corresponding two sum for each number
            two_sum = 0 - first_num
            # # Initialise difference dictionary to do two sum
            diff = {}
            for index, num in enumerate(nums):
                # If the second number is from different location as the first, find the difference
                # and add it to the dictionary
                if index != first_index:
                    difference = two_sum - num
                    if difference in diff:
                        triplet = sorted([first_num, difference, num])
                        if triplet not in final_array:
                            final_array.append(triplet)
                    diff[num] = index

        return final_array

        