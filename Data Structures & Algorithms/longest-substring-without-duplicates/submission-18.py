class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            r += 1

            res = max(res, len(window))

        return res
