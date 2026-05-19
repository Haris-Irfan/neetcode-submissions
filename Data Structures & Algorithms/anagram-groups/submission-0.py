class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalList = []
        for i in range(len(strs)):
            anagrams = []
            grouped = False
            currStr = strs[i]
            for groups in finalList:
                if currStr in groups:
                    grouped = True
            if grouped:
                continue
            print("Current String: ", currStr)
            anagrams.append(currStr)
            for j in range(i + 1, len(strs)):
                print("Current index: ", j)
                anagram = True
                queryStr = strs[j]
                print("Query String: ", queryStr)
                count = [0] * 26
                if len(currStr) == len(queryStr):
                    print("Same length string found!")
                    print("Comparing String: ", queryStr)
                    for k in range(len(currStr)):
                        count[ord(currStr[k]) - ord('a')] += 1
                        count[ord(queryStr[k]) - ord('a')] -= 1
                    print("Final count: ", count)
                
                    for val in count:
                        if val != 0:
                            anagram = False
                    
                    if anagram:
                        anagrams.append(queryStr)
                        print("Added!")
            
            finalList.append(anagrams)
            print("Output: ", finalList)
            print("\n")
        
        return finalList


