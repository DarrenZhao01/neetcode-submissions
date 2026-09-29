class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we can see which one to start on if there does not exist num - 1 in the array
        nums = set(nums)
        starts = set()

        max_seq = 0

        for num in nums:
            if (num - 1) not in nums:
                starts.add(num)
        
        for num in starts:
            curr = num
            curr_max = 1
            while (curr + 1) in nums:
                curr_max += 1
                curr += 1
            
            max_seq = max(curr_max, max_seq)

        return max_seq




