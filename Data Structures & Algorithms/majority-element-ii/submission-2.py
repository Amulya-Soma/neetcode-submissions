class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        result = []
        
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for j in freq.keys():
            if(freq[j]>len(nums)//3):
                result.append(j)
        return result
