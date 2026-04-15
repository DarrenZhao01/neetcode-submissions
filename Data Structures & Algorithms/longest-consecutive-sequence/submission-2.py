class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums: # this is the hardest part: How do we know where to start?
            # the solution: if there is a disconnect from the current number, meaning there is not number
            # one lower behind it, we can start counting from there.
                length = 1
                while num + length in nums:
                    length += 1
                longest = max(length, longest)
        return longest