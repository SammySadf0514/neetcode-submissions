class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left_idx = 0
        right_idx = 1
        res = []

        while left_idx < len(temperatures):
            if right_idx >= len(temperatures):
                res.append(0)
                left_idx += 1
                right_idx = left_idx + 1

            elif temperatures[right_idx] > temperatures[left_idx]:
                res.append(right_idx - left_idx)
                left_idx += 1
                right_idx = left_idx + 1

            else:
                right_idx += 1

        return res