class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_len = len(min(strs))
        result = ""
        for i in range(0,short_len):
            reference = strs[0][i]
            for s in range(1,len(strs)):
                if reference!=strs[s][i]:
                    return result
            result+=reference
        return result