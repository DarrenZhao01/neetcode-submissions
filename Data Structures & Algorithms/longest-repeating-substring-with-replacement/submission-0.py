class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        counts = {}
        max_freq = 0

        for right in range(len(s)):
            # 1. Expand window and update counts for the new character
            char = s[right]
            counts[char] = 1 + counts.get(char, 0)
            max_freq = max(max_freq, counts[char])
            # max_freq help us exclude the most common "different" character

            # 2. Check if window is invalid. If so, shrink from the left
            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            # 3. Update the result with the length of the current, valid window
            res = max(res, right - left + 1)
        
        return res