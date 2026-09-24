class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sol = set()

        for num in nums:
            if num in sol:
                return num
            sol.add(num)