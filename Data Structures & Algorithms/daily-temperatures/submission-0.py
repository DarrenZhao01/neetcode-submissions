class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)

        for i in range(n):
            count = 0
            return_bool = 0
            for k in range(i + 1, n):
                count += 1
                if temperatures[k] > temperatures[i]:
                    return_bool = 1
                    break
            if return_bool:
                res.append(count)
            else:
                res.append(0)
        
        return res