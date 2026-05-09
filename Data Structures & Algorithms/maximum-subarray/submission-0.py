class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxStreakSoFar = nums[0]
        currentStreakSum = nums[0]

        for i in range(1, len(nums)):
            
            currentStreakSum = max(nums[i], currentStreakSum + nums[i])
            maxStreakSoFar = max(maxStreakSoFar, currentStreakSum)

        return maxStreakSoFar