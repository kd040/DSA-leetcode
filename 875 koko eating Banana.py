class Solution:
    def totalHours(self, piles: list[int], speed: int) -> int:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # This is equivalent to math.ceil(pile / speed)
        return hours
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
       
        while low < high:
            mid = (low + high) // 2
            hours = self.totalHours(piles, mid)
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low  
    
def main():
    piles = [30,11,23,4,20]
    h = 6
    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    print(result)  # Output: 23
    
if __name__ == "__main__":
    main()
