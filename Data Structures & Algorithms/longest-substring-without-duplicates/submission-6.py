class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_len = 0

        for c in s:
            if c in window:
                while c in window:
                    window.pop(0)
                window.append(c)
            else:
                window.append(c)
                max_len = max(max_len, len(window))

        return max_len