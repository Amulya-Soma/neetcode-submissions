class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = [ch.lower() for ch in s if ch.isalnum()]
        print(sc)
        i = 0
        j = len(sc)-1
        while i<j:
            if(sc[i]!=sc[j]):
                return False
            i+=1
            j-=1
        return True