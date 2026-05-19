class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = {}

        for num in nums:
           freqCounter[num] = 1 + freqCounter.get(num, 0)

        topFreq = []
        
        for i in range(k):
            currHighest = max(freqCounter, key=freqCounter.get)
            topFreq.append(currHighest)
            freqCounter.pop(currHighest)

        return topFreq

    
