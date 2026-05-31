class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = {} 
        for s in strs:
            #sort the string
            # return a new list of string
            sorted_s = "".join(sorted(s))
            if sorted_s in resultDict:
                resultDict[sorted_s].append(s)
            else:
                resultDict[sorted_s] = [s]
        return list(resultDict.values())