class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = nums[i] ** 2
        result.sort()
        return result
        
def main():
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
if __name__ == "__main__":
    main()