class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in res:
                res[sortedS] = [s]
            else:
                res[sortedS].append(s)
        
        return list(res.values())