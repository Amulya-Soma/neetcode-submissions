class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicty = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            dicty[tuple(count)].append(s)
        result = []
        for i in dicty.keys():
            result.append(dicty[i])
        print(result)
        return result
        