class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicty = {}
        if len(s)!=len(t): return False
        for i in s:
            dicty[i] = dicty.get(i,0)+1
        for i in t:
            dicty[i] = dicty.get(i,0)-1
            if(dicty[i]==0):
                dicty.pop(i)
        print(dicty)
        return len(dicty)==0