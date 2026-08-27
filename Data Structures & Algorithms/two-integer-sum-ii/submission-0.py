class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left_idx = 0
        right_idx = n - 1
        sol = []
        for _ in range(n):
            left = numbers[left_idx]
            right = numbers[right_idx]
            if left + right < target:
                left_idx += 1
            elif left + right == target:
                sol.append(left_idx + 1)
                sol.append(right_idx + 1)
                return sol
            else:
                right_idx -= 1