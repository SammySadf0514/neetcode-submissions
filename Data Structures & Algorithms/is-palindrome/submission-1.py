class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "") # Truncate the string
        s = s.lower() # Lowercase
        s = "".join(char for char in s if char.isalnum()) # Remove special symbols
        news = s
        s = s[::-1] # Reverse The String
        if s == news:
            return True
        else:
            return False