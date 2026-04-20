class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            ch = s[i]
            freq[ch]=freq.get(ch,0)+1
        for i in range(len(t)):
            freq[t[i]] = freq.get(t[i],0)-1
            if(freq[t[i]]==0):
                del freq[t[i]]
        print(freq)
        return(len(freq)==0)
            