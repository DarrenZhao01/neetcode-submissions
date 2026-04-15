class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        res = 0
        for R in s:
            if R in window:
                while R in window:
                    window.pop(0)
                window.append(R)
            else:
                window.append(R)
                res = max(res, len(window))
        
        return res