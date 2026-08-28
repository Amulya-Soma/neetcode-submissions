class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R
        while(L<=R):
            k = (L+R)//2
            tot=0
            for i in piles:
                tot += math.ceil(i/k)
            if(tot<=h):
                R = k-1
                res = min(res,k)
            elif(tot>h):
                L = k+1
        return res