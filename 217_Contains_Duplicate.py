class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
def main():
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    print(solution.containsDuplicate(nums))  # Output: False

    nums = [1, 2, 3, 4, 1]
    print(solution.containsDuplicate(nums))  # Output: True
    
if __name__ == "__main__":
    main()
