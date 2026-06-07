class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        sCount, tCount = 52 * [0], 52 * [0]

        for i in range(len(t)):
            if ord(t[i]) - ord('A') > 25:
                tCount[ord(t[i]) - ord('a') + 26] += 1
            else:
                tCount[ord(t[i]) - ord('A')] += 1
               

        need = 0
        have = 0

        for i in range(52):
            if tCount[i] > 0:
                need += 1

        print("Starting matches:", have)
        # print("\n")
        l = 0
        minStr = ""

        for r in range(len(s) + 1):
            # print("Current Window:", s[l:r])
            # if have == need:
            #     print("Current Window Contains All Chars From t!")
            while have == need:
                query = s[l:r]
                # print("Current Query", query)
                if len(query) < len(minStr) or len(minStr) == 0:
                    minStr = query
                # print("Current Min String", minStr)

                if ord(s[l]) - ord('A') > 25:
                    index = ord(s[l]) - ord('a') + 26
                else:
                    index = ord(s[l]) - ord('A')
                sCount[index] -= 1

                if sCount[index] == tCount[index] - 1:
                    have -= 1
                    # print(f"Lost a match! {have} found.")

                l += 1

            if r == len(s):
                # print("End of sentence reached")
                break
            
            # print(f"Currently {have} matches. Adding {s[r]}")

            if ord(s[r]) - ord('A') > 25:
                index = ord(s[r]) - ord('a') + 26
            else:
                index = ord(s[r]) - ord('A')
            sCount[index] += 1

            if sCount[index] == tCount[index]:
                have += 1
            #     print(f"Found a match! {have} found.")

            # print("\n")
        
        # if minStr == "" and have == need:
        #     minStr = s[l:len(s)]

        return minStr
            


                    

                    
       