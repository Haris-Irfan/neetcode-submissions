class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        maxL = 0
        l,r = 0, 0

        while r < len(s):
            # print("Current Letter", s[r])
            # print("Current dictionary state", unique)
            if s[r] not in unique:
                unique[s[r]] = r
            else:
                # print(f"Character {s[r]} in dictionary")
                index = unique.get(s[r])
                # print(f"Removing from index {l} to {index}")
                for i in range(index - l + 1):
                    if s[l] in unique:
                        unique.pop(s[l])
                        l += 1
                unique[s[r]] = r                
                # print("Final state in dictionary", unique)
                # print("Final position of left pointer", l)
                # print("\n")

            maxL = max(r - l + 1, maxL)
            # print("Current maximum length", maxL)
            r += 1

        return maxL
