class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkPermutation(s1, s2):
            return sorted(s1) == sorted(s2)
        
        left = 0
        
        for right in range(len(s1), len(s2) + 1):
            if checkPermutation(s1, s2[left: right]):
                return True
            else:
                left += 1
        
        return False