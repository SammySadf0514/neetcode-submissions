class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            for m in matrix:
                n = len(m)
                if m[n - 1] < target:
                    continue
                elif m[n - 1] == target:
                    return True
                else:
                    middle = n // 2
                    if m[middle] == target:
                        return True
                    elif m[middle] < target:
                        for i in range(middle + 1, n):
                            if m[i] == target:
                                return True
                    else:
                        for i in range(0, middle):
                            if m[i] == target:
                                return True
            return False
