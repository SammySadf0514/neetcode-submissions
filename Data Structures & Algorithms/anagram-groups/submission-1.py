class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newMap = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in newMap:
                newMap[key] = []
            newMap[key].append(s)
        return list(newMap.values())
