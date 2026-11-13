class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq_s = {}
        letter_freq_t = {}

        for c in s:
            if c not in letter_freq_s:
                letter_freq_s[c] = 1
            else:
                letter_freq_s[c] += 1
        

        for c in t:
            if c not in letter_freq_t:
                letter_freq_t[c] = 1
            else:
                letter_freq_t[c] += 1
        
        return letter_freq_s == letter_freq_t