class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        final = ""
        for i in range(n):
            final+=word1[i]
            final+=word2[i]

        final+=word1[i+1:]
        final+=word2[i+1:]
        return final