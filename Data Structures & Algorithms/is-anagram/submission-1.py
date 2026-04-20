class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dicty1 = {}
        for i in range(0,len(s)):
            dicty1[s[i]] = dicty1.get(s[i],0)+1
            dicty1[t[i]] = dicty1.get(t[i],0)-1
        print(dicty1)
        return all (v==0 for v in dicty1.values())
        