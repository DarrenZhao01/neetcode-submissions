# dfs
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(curr_sum, curr_arr, curr_index): # curr_index to keep track of where we're at in the array
            if curr_sum == target:
                res.append(curr_arr.copy())
                return
            
            for j in range(curr_index, len(nums)):
                if curr_sum + nums[j] > target:
                    return

                curr_arr.append(nums[j])
                dfs(curr_sum + nums[j], curr_arr, j)
                curr_arr.pop() # processed
        
        dfs(0, [], 0)
        return res

# 2 5 6 9

# 2
# 2 5 6

# 2 2 = 4
# 2 5

# 2 2 2 = 6
# 2

# 2 2 2 2 = 8
# Nothing. Move back to previous.

# 2 2 2 = 6
# 2 (processed, popped)
# Nothing. Move back to previous.

# 2 2 = 4
# 2 (processed) 5

# 2 2 5 = 9
# # put in result
# Move back to previous

# 2 2 = 4
# 2 (processed) 5 (processed)
# Move back to previous

# 2
# 2 (processed) 5 6

# 2 5 = 7
# 2

# 2 5 2 = 9
# # already in result
# Move back to previous

# 2 5 = 7
# 2 (processed)
# Move back to previous

# 2
# 2 (processed) 5 (processed) 6

# ...


