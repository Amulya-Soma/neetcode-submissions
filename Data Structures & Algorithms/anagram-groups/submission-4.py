class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicty = defaultdict(list)
        for i in strs:
            count = [0]*26
            for ch in i:
                count[ord(ch)-ord('a')]+=1
            dicty[tuple(count)].append(i)
        result = []
        for i in dicty.keys():
            result.append(dicty[i])
        return result
