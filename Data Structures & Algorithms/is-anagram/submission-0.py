class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dicty1, dicty2 = {},{}
        for i in range(len(s)):
            dicty1[s[i]] = dicty1.get(s[i],0)+1
            dicty2[t[i]] = dicty2.get(t[i],0)+1
        print(dicty1, dicty2)
        return dicty1==dicty2