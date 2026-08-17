class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(i.lower() for i in s if i.isalnum())
        l = 0
        r = len(s_new)-1
        while(l<r):
            if(s_new[l]!=s_new[r]):
                return False
            l,r = l+1,r-1
        return True