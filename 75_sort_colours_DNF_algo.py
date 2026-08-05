class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low] #swap syntax in python [a ,b = b, a]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
def main():
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]

if __name__ == "__main__":
    main()