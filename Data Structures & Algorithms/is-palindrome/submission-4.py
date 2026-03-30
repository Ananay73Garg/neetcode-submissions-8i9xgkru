class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join([ch for ch in s if ch.isalpha() or ch.isdigit()])
        s = s.replace(" ","").lower()
        return (s==s[::-1])