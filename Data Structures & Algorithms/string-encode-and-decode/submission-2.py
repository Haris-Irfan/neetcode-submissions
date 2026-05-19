class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ""
        for s in strs:
            strLen = len(s)
            finalStr += str(strLen) + "#" + s
        
        print("Final String: ", finalStr)
        return finalStr



    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
            
        strLen = ""
        decodedArray = []
        strFound = False
        currIndex = 0

        while currIndex < len(s):
            currStr = s[currIndex]
            if strFound:
                length = int(strLen)
                string = s[currIndex : currIndex + length]
                print("String: ", string)
                decodedArray.append(string)
                print(decodedArray)
                currIndex = currIndex + length
                strLen = ""
                strFound = False
            elif currStr != '#':
                strLen += currStr
                print("String Length", strLen)
                currIndex += 1
            else:
                strFound = True
                currIndex += 1
        
        if len(decodedArray) == 0:
            decodedArray.append("")    

        return decodedArray

