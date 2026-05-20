class Solution:
    def trap(self, height: List[int]) -> int:
        currMax = 0
        maxIndex = 0
        prefix = len(height) * [0]
        suffix = len(height) * [0]

        for i in range(len(height)):
            if i < maxIndex:
                # print(f"Current index {i} smaller than max index {maxIndex} setting prefix to {height[maxIndex]}")
                # print("\n")
                prefix[i] = height[maxIndex]
                continue
            if i != len(height) - 1:
                preMax = height[i+1]
                maxIndex = i+1
                # print("Checking prefix of index", i)
                # print("Starting Maximum", preMax)
                # print("Starting index", maxIndex)
                # print("\n")
            else:
                # print(f"One element after {height[i]}, using last element")
                # prefix[i] = height[i+1]
                # print(f"Value at index {i} = {prefix[i]}")
                break
            for j in range(i+1, len(height)):
                # print("Query:")
                # print("Current Number", height[j])
                # print("Current Index", j)

                if height[j] > preMax:
                    preMax = height[j]
                    maxIndex = j
                # print("Results:")
                # print("New maximum", preMax)
                # print("New index", maxIndex)
                # print("\n")
            prefix[i] = preMax


        maxIndex = len(height) - 1
        for i in range(len(height) - 1, -1, -1):
            if i > maxIndex:
                suffix[i] = height[maxIndex]
                continue
            if i > 0:
                sufMax = height[i-1]
                maxIndex = i-1
            else:
                break
            for j in range(i-1, -1, -1):
                if height[j] > sufMax:
                    sufMax = height[j]
                    maxIndex = j
                suffix[i] = sufMax

        print("Prefix Max", prefix)
        print("Suffix Max", suffix)

        for i in range(len(height)):
            trapped = min(prefix[i], suffix[i]) - height[i]
            if trapped > 0:
                currMax += trapped

        return currMax
