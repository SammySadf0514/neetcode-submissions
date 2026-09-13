class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        res = 1
        count = 1
        x = nums[0]
        for i in range(1, len(nums)):
            if x + 1 == nums[i]:
                count += 1
            else:
                count = 1
            res = max(res, count)
            x = nums[i]

        return res