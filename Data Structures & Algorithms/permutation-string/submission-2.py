class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        w1 = {}
        w2 = {}
        for i in range(len(s1)):
            w1[s1[i]] = w1.get(s1[i],0)+1
        for R in range(0,len(s2)):
            w2[s2[R]] = w2.get(s2[R],0)+1
            while (R-L+1>len(s1)):
                w2[s2[L]]-=1
                if(w2[s2[L]]==0): w2.pop(s2[L])
                L+=1
            if(w1==w2):
                return True
        return False