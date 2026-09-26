class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        seen = {}

        for i in range(n):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i


    seen = {4:0, 5:1, }
