class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxL = 0
        charDict = {}

        while r < len(s):
            print(f"Word pointed at by left pointer at index {l}, {s[l]}")
            print(f"Word pointed at by right pointer at index {r}, {s[r]}")
            print("Current state of dictionary", charDict)
            curr = s[r]
            charDict[curr] = charDict.get(curr, 0) + 1
            maxFreq = max(charDict.values())
            subs = r - l + 1 - maxFreq
            print("Number of words that need to be substituted", subs)
            if subs > k:
                print("Replacements exceeds limit, shifting left pointer")
                charDict[s[l]] = charDict.get(s[l], 0) - 1
                l +=1

            print("\n")

            maxL = max(r - l + 1, maxL)

            r += 1

        return maxL
        