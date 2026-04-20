class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')]+=1
            freq[tuple(count)].append(s)
        print(freq.values())
        return list(freq.values())