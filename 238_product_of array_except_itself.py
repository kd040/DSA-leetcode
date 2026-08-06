class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        # Calculate left products
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
def main():
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))  # Output: [24, 12, 8, 6]
if __name__ == "__main__":
    main()