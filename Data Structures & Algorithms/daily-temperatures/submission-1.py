class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left_idx = 0
        res = []

        while left_idx < len(temperatures):
            right_idx = left_idx + 1
            count = 0

            while right_idx < len(temperatures):
                if temperatures[right_idx] > temperatures[left_idx]:
                    count = right_idx - left_idx
                    break

                right_idx += 1

            res.append(count)
            left_idx += 1
        return res