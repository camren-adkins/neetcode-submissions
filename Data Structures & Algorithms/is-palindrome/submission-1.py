class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        firstHalf = set(s[:len(s)//2])
        return set(s[(len(s)+1)//2:]) == firstHalf