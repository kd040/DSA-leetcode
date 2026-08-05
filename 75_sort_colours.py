class Solution:
    def sortColors(self, nums: list[int]) -> None:
       #counts of each color
        count_0 = 0
        count_1 = 0
        count_2 = 0

        # Count occurrences of each color
        for num in nums:
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1

        # Fill the array with the counted values
        i = 0
        while count_0 > 0:
            nums[i] = 0
            i += 1
            count_0 -= 1

        while count_1 > 0:
            nums[i] = 1
            i += 1
            count_1 -= 1

        while count_2 > 0:
            nums[i] = 2
            i += 1
            count_2 -= 1
            
            
def main():
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]  
    
    
if __name__ == "__main__":
        main()