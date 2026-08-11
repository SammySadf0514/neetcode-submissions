class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []


        for num in operations:
            if num == "+":
                res.append(res[-1] + res[-2])
            elif num == "C":
                res.pop()
            elif num == "D":
                res.append(2 * res[-1])
            else:
                num = int(num)
                res.append(num)

        return sum(res)