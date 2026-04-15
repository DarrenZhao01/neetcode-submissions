class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # Adds 1 to the existing count of the current character.
                                                    # The '0' is the default
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# Creates letter-frequency table and compares whether they are the same.