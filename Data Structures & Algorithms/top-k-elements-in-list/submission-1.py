# put it into a dict where the dict is the number frequency table, and then sort by most to least, then pull first K
# bucket sort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        arr = []
        for num, f in freq.items():
            arr.append([f, num])
        
        arr.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(arr[i][1])

        return res