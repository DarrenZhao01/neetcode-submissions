class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}

        for num in nums: # build the freq table
            if num not in freq_list:
                freq_list[num] = 1
            else:
                freq_list[num] += 1
        
        arr = []

        for num, count in freq_list.items(): # reversing the num and count so that the array can be sorted by frequency of the number.
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res