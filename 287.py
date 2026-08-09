class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0    
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

def main():
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
if __name__ == "__main__":
    main()  