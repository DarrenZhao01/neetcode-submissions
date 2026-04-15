class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        mid = n // 2

        while l <= r:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1 # we also need to skip the mid one
                mid = (l + r) // 2
            else:
                l = mid + 1 # we need to skip the mid one
                mid = (l + r) // 2
        
        return -1