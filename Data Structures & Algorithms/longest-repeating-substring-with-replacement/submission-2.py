class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        res = 0

        count = {}

        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            windowSize = right - left + 1

            if windowSize - max(count.values()) <= k:
                res = max(res, windowSize)
            else:
                count[s[left]] -= 1
                left += 1
            right += 1

        return res