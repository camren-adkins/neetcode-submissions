class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = dict()
        count_t = dict()
        for char in s:
            if char in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1
        for char in t:
            if char in count_t:
                count_t[char] = count_t[char] + 1
            else:
                count_t[char] = 1
        return (count == count_t)
