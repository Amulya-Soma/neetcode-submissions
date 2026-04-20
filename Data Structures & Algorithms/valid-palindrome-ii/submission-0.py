class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin(l,r):
            while(l<r):
                if(s[l]!=s[r]):
                    return False
                l+=1
                r-=1
            return True
        
        sc = "".join(ch for ch in s if ch.isalnum())
        l = 0
        r = len(sc)-1
        while l<r:
            if(sc[l]!=sc[r]):
                return is_palin(l+1,r) or is_palin(l,r-1)
            l+=1
            r-=1
        return True
        