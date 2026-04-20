class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        def ispalin(a,b):
            while a<b:
                if s[a]!=s[b]:
                    return False
                a+=1
                b-=1
            return True
        while i<j:
            if s[i]!=s[j]:
                return ispalin(i+1,j) or ispalin(i,j-1)
            i+=1
            j-=1
        return True