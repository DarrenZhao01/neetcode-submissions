class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        countZeroPositions = []
        n = len(nums)
        total_product = nums[0]

        for i in range(n):
            if nums[i] == 0:
                countZeroPositions.append(i)

        if len(countZeroPositions) >= 2:
            return [0]*n
        elif len(countZeroPositions) == 1:
            for i in range(1, n):
                if nums[i] != 0:
                    total_product *= nums[i]
            res = [0] * n
            res[countZeroPositions[0]] = total_product
            return res
        
        res = []
        for i in range(1, n):
            total_product *= nums[i]

        for i in range(n):
            res.append(total_product // nums[i])
        
        return res