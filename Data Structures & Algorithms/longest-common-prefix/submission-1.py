class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(min(strs))
        res = ""
        for i in range(n):
            ref = strs[0][i]
            for j in range(1,len(strs)):
                if(ref!=strs[j][i]):
                    return res
            res+=ref
        return res