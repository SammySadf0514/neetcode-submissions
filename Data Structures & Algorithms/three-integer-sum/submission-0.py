class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prevMap = {}
        for i, n in enumerate(nums):
            if n in prevMap:
                continue
            else:
                prevMap[n] = i

        res = []
        seen = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                needed = -(nums[i] + nums[j])

                if needed in prevMap:
                    k = prevMap[needed]

                    if k != i and k != j:
                        triplet = [nums[i], nums[j], needed]
                        triplet.sort()

                        if tuple(triplet) not in seen:
                            seen.add(tuple(triplet))
                            res.append(triplet)
        return res