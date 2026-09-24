class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        return set(s[(len(s)+1)//2:]) == set(s[:len(s)//2])