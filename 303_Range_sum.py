class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sum = [0] * len(nums)

        self.prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]


def main():
    nums = [-2, 0, 3, -5, 2, -1]

    num_array = NumArray(nums)

    print(num_array.sumRange(0, 2))  # 1
    print(num_array.sumRange(2, 5))  # -1
    print(num_array.sumRange(0, 5))  # -3


if __name__ == "__main__":
    main()