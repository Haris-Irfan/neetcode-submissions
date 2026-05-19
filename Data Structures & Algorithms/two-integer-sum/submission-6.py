class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        print(sortedNums)
        low = 0
        high = len(sortedNums) - 1
        while sortedNums[low] + sortedNums[high] != target:
            currSum = sortedNums[low] + sortedNums[high]
            print(currSum)
            if currSum < target:
                low += 1
            elif currSum > target:
                high -= 1

        firstIndex = nums.index(sortedNums[low])
        secondIndex = nums.index(sortedNums[high])

        if secondIndex == firstIndex:
            remainderNums = nums[firstIndex + 1:]
            print(remainderNums)
            secondIndex = remainderNums.index(sortedNums[high]) + firstIndex + 1

        return sorted([firstIndex, secondIndex])
    
        