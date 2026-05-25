class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxL = 0
        charDict = {}

        while r < len(s):
            curr = s[r]
            charDict[curr] = charDict.get(curr, 0) + 1
            maxFreq = max(charDict.values())
            subs = r - l + 1 - maxFreq
            while subs > k:
                charDict[s[l]] = charDict.get(s[l], 0) - 1
                l +=1
                maxFreq = max(charDict.values())
                subs = r - l + 1 - maxFreq
            maxL = max(r - l + 1, maxL)

            r += 1

        return maxL
        