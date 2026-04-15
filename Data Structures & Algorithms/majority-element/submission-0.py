class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) / 2
        nums_freq = {}

        for num in nums: # build the freq table
            if num not in nums_freq:
                nums_freq[num] = 1
            else:
                nums_freq[num] += 1
        
        for num, freq in nums_freq.items(): # find the one that crosses the n/2 majority
            if freq > threshold:
                return num