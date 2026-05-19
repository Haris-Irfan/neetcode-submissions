class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while True:
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1

            if start >= end:
                break

            print("Front Letter: ", s[start])
            print("Back Letter: ", s[end])
            print("\n")

            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    print("Fail!")
                    return False

                start += 1
                end -= 1

        return True