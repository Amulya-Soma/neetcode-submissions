class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first,second = 0,0
        res = []
        a,b = len(word1),len(word2)
        while(first<a or second<b):
            if(first<a):
                res.append(word1[first])
            if(second<b):
                res.append(word2[second])
            first+=1
            second+=1
        return "".join(res)