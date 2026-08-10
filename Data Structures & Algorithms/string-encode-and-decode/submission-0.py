class Solution:

    def encode(self, strs: List[str]) -> str:
        result = " ".join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        result = s.split(" ")
        return result
