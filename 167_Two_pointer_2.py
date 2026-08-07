class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left =0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
def main():
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))  # Output: [1, 2]
if __name__ == "__main__":
    main()