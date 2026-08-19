class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        news = s
        s = s[::-1]
        if s == news:
            return True
        else:
            return False