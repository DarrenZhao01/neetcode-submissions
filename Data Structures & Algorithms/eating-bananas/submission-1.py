class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Example:
        # Piles = [1,4,3,2], h = 9

        # k=1 → 10 hours (invalid)
        # k=2 → 6 hours (valid)
        # k=3 → 5 hours (valid)
        # k=4 → 4 hours (valid)
        # k=5 -> 4 hours(valid)
        # k=6 -> 4 hours(valid)

        # the search space is 1 to max(piles)
        
        def totalHours(piles, k) -> int:

            totalHours = 0

            for pile in piles:
                totalHours += math.ceil(pile / k)
            
            return totalHours
        
        l = 1
        r = max(piles)
        res = r

        

        while (l <= r):
            mid = (l + r) // 2
            hours = totalHours(piles, mid)

            if hours > h:
                l = mid + 1
            elif hours <= h:
                res = mid
                r = mid - 1
            else:
                return res
    
        return res