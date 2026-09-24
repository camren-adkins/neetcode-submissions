class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum,s)).lower()
        for x, char in enumerate(s[:(len(s)+1)//2]):
            if char != s[len(s)-1-x]:
                return False
        return True    