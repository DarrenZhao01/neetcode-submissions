class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_freq = {}
        for word in strs:
            generalized_word = tuple(sorted(word)) # sorted() gives a list
            if generalized_word not in word_freq: # dict keys cannot be mutable
                word_freq[generalized_word] = [word]
            else:
                word_freq[generalized_word].append(word)
        
        res = list(word_freq.values())
        return res
