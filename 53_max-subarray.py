class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = int(-1e9)
        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum
    
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))  
    
if __name__ == "__main__":
    main()