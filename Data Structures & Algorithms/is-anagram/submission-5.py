class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicty = {}
        for i in s:
            dicty[i] = dicty.get(i,0)+1
        print(dicty)
        for j in t:
            dicty[j] = dicty.get(j,0)-1
            if(dicty[j]==0):
                del dicty[j]
        print(dicty)
        return len(dicty)==0