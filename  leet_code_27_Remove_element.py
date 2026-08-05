class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k

if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    k = Solution().removeElement(nums, val)
    print(k)
    print(nums[:k])
    