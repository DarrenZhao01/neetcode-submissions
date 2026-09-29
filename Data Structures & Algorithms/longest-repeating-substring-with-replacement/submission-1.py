class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABBABAAA, k = 2 AAAABBA
        # window: A
        # {A:1, }
        # we will use a window
        # if the window contains a window.length - max letter frequency that is larger than k after we widen the window to the right, then we will narrow the window from the left until the the max l
        l = 0
        letter_freq = {}
        max_length = 0
        window = []

        for r in range(len(s)):
            window.append(s[r])
            if s[r] not in letter_freq:
                letter_freq[s[r]] = 1
            else:
                letter_freq[s[r]] += 1

            while ((r - l + 1) - max(letter_freq.values())) > k:
                letter_freq[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length


            
