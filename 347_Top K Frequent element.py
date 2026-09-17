class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_map[:k]] 