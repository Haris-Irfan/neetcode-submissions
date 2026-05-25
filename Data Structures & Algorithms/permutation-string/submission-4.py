class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for c in s1:
            s1_arr[ord(c) - ord('a')] += 1

        for i in range(len(s2)- len(s1) + 1):
            # if len(s2[i:i+len(s1)]) < len(s1):
            #     break
            # else:
            for j in range(i, i+len(s1)):
                s2_arr[ord(s2[j]) - ord('a')] += 1
            if s2_arr == s1_arr:
                return True
            s2_arr = [0] * 26

        return False
                
        