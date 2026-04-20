class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setwindow = set()
        l = 0
        res = 0
        for r in range(len(s)):
            # WHILE there are duplicates in the window, move the window towards right
            while s[r] in setwindow:
                setwindow.remove(s[l])
                l+=1
            setwindow.add(s[r])
            res = max(res,r-l+1)
        return res