class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxx = 0
        window = {}
        for R in range(0,len(s)):
            window[s[R]] = window.get(s[R],0)+1
            while ((R-L+1)-max(window.values())>k):
                window[s[L]]-=1
                L+=1
            maxx = max(maxx,R-L+1)
        return maxx