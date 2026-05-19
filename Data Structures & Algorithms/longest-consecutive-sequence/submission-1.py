class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        currHighest = 0
        for num in nums:
            count = 1
            prevNum = num - 1
            while prevNum in numSet:
                count += 1
                prevNum -= 1
            if count > currHighest:
                currHighest = count
        
        return currHighest

