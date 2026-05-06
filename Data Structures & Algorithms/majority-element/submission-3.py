class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        limit = n // 2

        letter_freq = {}
        
        for i in nums:
            if i in letter_freq:
                letter_freq[i] += 1
                if letter_freq[i] > limit:
                    return i
            else:
                letter_freq[i] = 1
                if letter_freq[i] > limit:
                    return i
