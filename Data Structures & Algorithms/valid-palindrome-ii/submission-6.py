class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        def check_palin(left,right):
            while(left<=right):
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        while(l<r):
            if s[l]!=s[r]:
                return check_palin(l+1,r) or check_palin(l,r-1)
            l+=1
            r-=1
        return True