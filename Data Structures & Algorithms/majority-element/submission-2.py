class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        # res = 0
        for i in nums:
            freq[i] = freq.get(i,0)+1
        print(freq)
        for i in freq.keys():
            if(freq[i]>len(nums)//2):
                return i
        # print(res)
        # return res