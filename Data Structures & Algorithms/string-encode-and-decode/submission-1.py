class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length = len(string)
            encoded_string += str(length) + "#" + string
        return encoded_string



    def decode(self, s: str) -> List[str]:
        decoded_string = []
        pointer = 0

        while pointer < len(s):
            hash_index = s.find("#", pointer)
            length = int(s[pointer : hash_index])
            start = hash_index + 1
            end = start + length
            decoded_string.append(s[start : end])
            pointer = end
        return decoded_string