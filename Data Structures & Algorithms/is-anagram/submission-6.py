class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicty = {}
        for i in s:
            dicty[i] = dicty.get(i,0)+1
        for i in t:
            dicty[i] = dicty.get(i,0)-1
            if(dicty[i]==0):
                del(dicty[i])
        print(dicty)
        return len(dicty)==0

