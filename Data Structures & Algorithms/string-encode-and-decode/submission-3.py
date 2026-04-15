class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str = encoded_str + f'{len(word)}#{word}'
        return encoded_str
    
    
    def decode(self, s: str) -> List[str]:
        res = []
        while s != "":
            j = 0
            while s[j] != '#':
                j += 1
            length = int(s[:j])
            word_to_store = s[j + 1:length + 1 + j]
            res.append(word_to_store)
            s = s[length + 1 + j:]
        return res
