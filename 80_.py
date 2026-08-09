class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        slow  = 1
        count = 1

        for read_index in range(0, len(nums) - 1):
            if nums[read_index + 1] == nums[read_index]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[slow] = nums[read_index + 1]
                slow += 1

        return slow

def main():
    nums = [1, 1, 1, 2, 2, 3]
    new_length = Solution().removeDuplicates(nums)
    print(new_length)  # Output: 5
    print(nums[:new_length])  # Output: [1, 1, 2, 2, 3]
if __name__ == "__main__":
    main()