class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        left_idx = 0
        right_idx = len(height) - 1

        left_max = 0
        right_max = 0

        while left_idx < right_idx:

            if height[left_idx] <= height[right_idx]:

                if height[left_idx] >= left_max:
                    left_max = height[left_idx]
                else:
                    water += left_max - height[left_idx]

                left_idx += 1

            else:

                if height[right_idx] >= right_max:
                    right_max = height[right_idx]
                else:
                    water += right_max - height[right_idx]

                right_idx -= 1

        return water